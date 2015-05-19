import re
import csv
import os

the_dir = "/Users/hah661/Documents/Northwestern/MyPHD/social_policy_course/SocPol_Video/transcript_txts/"

walker = os.walk(the_dir)
for thing in walker:
	files = [filename for filename in thing[2] if ".txt" in filename and "csv" not in filename]

# infile = open(the_dir + 'W2014_1.txt', 'rU')
# outfile = open(the_dir + 'W2014_1.csv', 'w')


def timestamp_to_seconds(timestamp):
    hr = float(timestamp[:2])
    min = float(timestamp[3:5])
    sec = float(timestamp[6:8])
    centisec = float(timestamp[9:11]) / 100
    return str(hr * 60 * 60 + min * 60 + sec + centisec)


outfile = open(the_dir +'all_out.csv', 'w')
writer = csv.DictWriter(outfile, fieldnames =['start', 'end', 'speaker', 'spoken'])
writer.writeheader()


for the_file in files:
	infile = open(the_dir+the_file, 'rU')
	for line in infile.read().split("\n")[1:]:
	    if len(line) > 0:
	        regex = '\\[(\\d{2}:\\d{2}:\\d{2}.\\d{2})\\](.+?):(.*?)\\[(\\d{2}:\\d{2}:\\d{2}.\\d{2})\\]'
	        p = re.compile(regex)
	        m = p.match(line)
	        if m:
	        	adict = {}
	        	adict['start'] = timestamp_to_seconds(m.groups()[0])
	        	adict['end'] = timestamp_to_seconds(m.groups()[3])
	        	adict['speaker'] = the_file+m.groups()[1]
	        	adict['spoken'] =  m.groups()[2]
	        	adict['spoken'] = adict['spoken']
	        	adict['spoken'] = adict['spoken'].replace(","," ")

	        	# adict['spoken'] = adict['spoken'].replace("","")
	        	
	        	writer.writerow(adict)
	infile.close()
outfile.close()	
