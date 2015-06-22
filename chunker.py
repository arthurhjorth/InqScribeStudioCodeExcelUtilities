## a chunker can receieve anything, but must return a list of dictionaries with spoken words
## so from an interface point of view, all it must do is have a method that
## returns a Text  (Text objects MUST contain their text, so the constraint is there)

import nltk

class Chunker:

	def getText(self, alist):
		a = ""