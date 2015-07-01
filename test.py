import chunker as c
import xml_writer as x
# import chunks
import CentroidClusterModule
from CentroidClusterModule import CentroidClusterModule
import nltk
import csv
import Minute_chunker 
import FileImporter
import TagHandler


the_dir = '/Users/hah661/Documents/Northwestern/MyPHD/social_policy_course/SocPol_Video/transcript_txts/'
files = [
'F2014_1.txtout.csv',
'F2014_2.txtout.csv',
'F2014_3.txtout.csv',
'F2014_4.txtout.csv',
'F2014_5.txtout.csv',
'W2014_1.txtout.csv',
'W2014_2.txtout.csv',
'W2014_3.txtout.csv',
'W2014_4.txtout.csv'
]

all_spoken = []
for filename in files:
	 all_spoken = all_spoken + FileImporter.import_file(the_dir+filename)

chunk_tags = Minute_chunker.chunk(all_spoken)

all_spoken = TagHandler.apply_tags(all_spoken, chunk_tags, "minute_chunk")

all_spoken = TagHandler.remove_tag(all_spoken, "minute_chunk")




x = CentroidClusterModule()



