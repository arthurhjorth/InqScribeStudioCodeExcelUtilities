

## a chunker is a very simple thing. It just returns a list of tags given the 
## text that is provided, based on end times. Because time is already in seconds
## we can just divide by the time_in_seconds for the chunks we want

import nltk
def chunk(alist, time_in_seconds = 60):
	tags = []	
	counter = 0
	return [int(float(entry['end']) / time_in_seconds) for entry in alist]