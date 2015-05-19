
# this class takes a list of chunks and writes them to an xml file that StudioCode understands.
# each list will result in a new xml file -> a new timeline 'code' in StudioCode.


# a chunk looks like this:
# {'spoken': ' Park wise yeah. ', 'start': '3657.28', 'speaker': 'W2014_1.txt Right person', 'end': '3660.11'},
def write_chunks(chunks, code_name, fileoutname, split_rows = False):
	outfile = open(fileoutname, 'w')
	instances = 1
    # get information from the regex match object
	for chunk in chunks:
		start = chunk['start']
		end = chunk['end']
		speaker = chunk['speaker']
		spoken = chunk['spoken']
		# now write xml
		outfile.write("<instance>")
		outfile.write("<ID>" + str(instances) + "</ID>")
		outfile.write("<start>" + str(start) + "</start>")
		outfile.write("<end>" + str(end) + "</end>")
		if split_rows:
			outfile.write("<code>" + str(speaker) + "</code>")
		else:
			outfile.write("<code>Transcript</code>")    
			outfile.write("<free_text>" + str(spoken) + "</free_text>")
			outfile.write("</instance>")
# add one to counter
		instances = instances + 1
		outfile.close()

