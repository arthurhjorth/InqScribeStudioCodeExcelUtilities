import csv
import nltk
import re


the_lambda  = lambda x: 'income' in words_inside_chunk(x)


def words_inside_chunk(achunk):
	return nltk.word_tokenize("".join(map (lambda y: y['spoken'], achunk)).lower())


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
		if float(line['start']) > counter * duration_in_seconds:
			all_chunks.append(a_chunk)
			a_chunk = []
			counter = counter + 1


	return filter(the_lambda, all_chunks)

print chunk('/Users/hah661/Documents/Northwestern/MyPHD/social_policy_course/SocPol_Video/transcript_txts/F2014_3.txtout.csv', 120, the_lambda)