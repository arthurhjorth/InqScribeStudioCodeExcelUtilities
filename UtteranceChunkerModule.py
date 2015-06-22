

## a chunker can receieve anything, but must return a list of dictionaries with spoken words
## so from an interface point of view, all it must do is have a method that
## returns a Text  (Text objects MUST contain their text, so the constraint is there)

# Note to self: ALL a chunker should do is combine text inside the dictionaries and provide end and
# start timestamps. We can use the timpe stamps in the new chunks to find the original text, speakers
# etc.

import nltk
def chunk(alist):
	print [thing['spoken'] for thing in alist]