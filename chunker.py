import csv
import nltk
import re
import sys  

reload(sys)  
sys.setdefaultencoding('utf8') #i don't know why i need this, but I do

# the_lambda  = lambda x: 'income' in words_inside_chunk(x)


def words_inside_chunk(achunk):
	the_spoken = "".join(map (lambda y: y['spoken'], achunk)).lower()
	return nltk.word_tokenize(the_spoken)


# optional filtering lambda on words
def chunk(the_input_file, duration_in_seconds, the_lambda = lambda x: True):
	counter = 0
	all_chunks = []
	a_chunk = []

	# we create a list of chunks. Each chunk contains a list of dictionaries with spaker, startime, endtime, spoken.
	# outer: all chunks
	# inner: a chunk
	## dictionar: utterance_data

	infile = open(the_input_file, 'r')
	reader = csv.DictReader(infile)
	for line in reader:
		a_chunk.append(line)
		print line['start']
		if float(line['start']) > counter * duration_in_seconds:
			all_chunks.append(a_chunk)
			a_chunk = []
			counter = counter + 1


	return filter(the_lambda, all_chunks)

