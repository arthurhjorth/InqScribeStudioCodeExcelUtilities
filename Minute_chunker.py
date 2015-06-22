

## a chunker can receieve anything, but must return a list of dictionaries with spoken words
## so from an interface point of view, all it must do is have a method that
## returns a Text  (Text objects MUST contain their text, so the constraint is there)

# Note to self: ALL a chunker should do is combine text inside the dictionaries and provide end and
# start timestamps. I think. We can use the timpe stamps in the new chunks to find the original text, speakers
# etc.

import nltk
def chunk(alist, time_in_seconds = 60):
	counter = 0
	chunk = {}
	outer = []
	last_end_time = 0
	for thing in alist:
		if 'start' not in chunk.keys():
			chunk['start'] = thing['start']
		if float(thing['end']) > counter * time_in_seconds:
			chunk['end'] = last_end_time
			outer.append(chunk)
			chunk = {}
			chunk['spoken'] = ""
			counter = counter + 1
		chunk['spoken'] = chunk['spoken'] + thing['spoken']
		last_end_time = thing['end']
	return outer[1:]

