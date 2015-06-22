# the main purpose of a Text object is to act as a container for both the original text
# and the working-copy of a text. This is where the modules API belongs.

# each of these contain chunk dictionaries
utterances = []

# I am not sure this belongs here, but maybe it does. It's kinda neat if it always follows

class Text:
	# chunked text is a list of dictionaries
    def __init__(self, chunked_text):
    	original_text = chunked_text
    	working_text = original_text
    

    ###################################################################################################
    ## This is the other API - actually it shouldn't have one. It should just take  
    ## a Text object and create a new one without tags and with altered working_text
    ###################################################################################################
    # this takes a list of new uttereances and puts them inside the 
    # working text dictionary
    def update_working_text(new_working_text):
    	for n in range(len(new_working_text)):
    		utterances[n]['working_text'] = new_working_text[n]

    
	###################################################################################################
    ## this is basically the modules API as I think of it. It can get a copy of the working
    ## uttereances, and it can add tags to them (or remove them). That's it. And I think that's best.
    ###################################################################################################
    def working_utterances():
    	return [utterance['working_text'] for utterance in utterances]
    # this takes a dictionary in which the key is a tag,
    # and the value is a list of the value of that tag for each of the utterances
    # in the working_text
    # this prevents people to change the working text
    def add_tags(new_tags):
    	for tag in new_tags:
    		for n in range(len(new_tags[tag])):
    			utterance[n]['tags'][tag] = new_tags[tag][n]
        # remove all tags with a particular name
    def remove_tags(tagname):
    	for utterance in utterances:
    		utterance['tags'].pop(tagname, None)