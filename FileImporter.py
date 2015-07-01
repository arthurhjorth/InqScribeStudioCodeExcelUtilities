## the purpose of this class is to help import files. Because we want everything to be tags, 
## all this really does is take a csv file, add the file name to each entry, and sends that back
## as a list of dictionaries

import csv



def import_file(filename, encoding = 'U'):
	reader = csv.DictReader(open(filename, 'r'+encoding))
	data = [thing for thing in reader]
	for thing in data:
		thing['id'] = str(data.index(thing))
		thing['file'] = filename
	return data