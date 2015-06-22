import chunker as c
import xml_writer as x
# import chunks
import CentroidClusterModule
from CentroidClusterModule import CentroidClusterModule
import nltk
import csv
import Minute_chunker 


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

all_chunked = {}
for filename in files:
	reader = csv.DictReader(open(the_dir+filename, 'rU'))
	data = [thing for thing in reader]
	all_chunked[filename] = Minute_chunker.chunk(data)


print all_chunked

# print chunked_data
x = CentroidClusterModule()

