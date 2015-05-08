import sys
import re

# if we want to calculate the end times, first create the entire thing, and 

# take in parameter here 
name = str(sys.argv[1])
if len(sys.argv) > 2:
    if sys.argv[2] == "true":
        split_rows = True
else: 
    split_rows = False
#print split_rows
path = sys.path[0]


'''
ADD CODE HERE TO PASS A REGEX AS A PARAMETER
for now, just set the_regex to a blank string
'''
the_regex = ""
full_file = path + "/" + name

infile = open(full_file, 'r')
outfile_name = full_file.split(".")[0] + "_out.xml"
outfile = open(outfile_name, 'w')

outfile.write("<file><ALL_INSTANCES>")

'''
This contains last lines timestamp so I can write it later for those that don't have
end time stamps.
'''

#this is the function that we call to write the xml
the_write_function = ""

instances = 1

def build_xml_endstamp(m):
    global instances 
    # get information from the regex match object
    start = m.groups()[0]
    end = m.groups()[3]
    speaker = m.groups()[1]
    spoken = m.groups()[2]
    # now write xml
    outfile.write("<instance>")
    outfile.write("<ID>" + str(instances) + "</ID>")
    outfile.write("<start>" + timestamp_to_seconds(start) + "</start>")
    outfile.write("<end>" + timestamp_to_seconds(end) + "</end>")
    if split_rows:
        outfile.write("<code>" + str(speaker) + "</code>")    
    else:
        outfile.write("<code>Transcript</code>")    
    outfile.write("<free_text>" + spoken + "</free_text>")
    outfile.write("</instance>")
    # add one to counter
    instances = instances + 1

def build_xml_wo_endstamp(m):
    global instances 
    global last_end_time
    # get information from the regex match object
    start = m.groups()[0]
    speaker = m.groups()[1]
    spoken = m.groups()[2]
    '''
     now write xml
     first we end last instance's information by putting in the end stamp as
     the current time's start minus one centisecond
    we only do this if we are not at instance 0
    '''
    if instances != 1:
        outfile.write("<end>" + str(float(timestamp_to_seconds(start)) - .01) + "</end>")
        outfile.write("</instance>")

    outfile.write("<instance>")
    outfile.write("<ID>" + str(instances) + "</ID>")
    outfile.write("<start>" + timestamp_to_seconds(start) + "</start>")
    if split_rows:
        outfile.write("<code>" + str(speaker) + "</code>")    
    else:
        outfile.write("<code>Transcript</code>")    
    outfile.write("<free_text>" + spoken + "</free_text>")
    # add one to counter
    instances = instances + 1

def timestamp_to_seconds(timestamp):
    hr = float(timestamp[:2])
    min = float(timestamp[3:5])
    sec = float(timestamp[6:8])
    centisec = float(timestamp[9:11]) / 100
    return str(hr * 60 * 60 + min * 60 + sec + centisec)


alist = infile.read().split("\r")
first_line = alist[0]

if the_regex == "":
    regex = '\\[(\\d{2}:\\d{2}:\\d{2}.\\d{2})\\](.+?):(.*?)\\[(\\d{2}:\\d{2}:\\d{2}.\\d{2})\\]'
    p = re.compile(regex)
    m = p.match(first_line)
    if m:
        print "Creating xml for transcription WITH end timestamps."
        print "If this is not correct, your file format is bad"
        the_regex = regex
        the_write_function = build_xml_wo_endstamp
    regex = '\\[(\\d{2}:\\d{2}:\\d{2}.\\d{2})\\](.+?):(.*?)'
    p = re.compile(regex)
    m = p.match(first_line)
    if m:
        print "Creating xml for transcription WITHOUT end timestamps"
        print "If this is not correct, your file format is bad"
        the_regex = regex
        the_write_function = build_xml_wo_endstamp
# compile the IDed regex

    
# now write the xml
#[the_write_function(p.match(line)) for line in alist]
for line in alist:
    p = re.compile(the_regex)
    m = p.match(line)
    if m:
        the_write_function(m)

# special case for without end timestamp: add a timestamp + end time of something ridiculously high
if the_write_function == build_xml_wo_endstamp:
    outfile.write("<end>9999999999999999999999999999999999999999999999</end>")
    outfile.write("</instance>")


outfile.write("</ALL_INSTANCES></file>")
infile.close()
outfile.close()