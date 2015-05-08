import csv
import xml
import os
import xml.etree.ElementTree as ET

input_file = open('Transcription2.xml')

tree = ET.parse(input_file)
root = tree.getroot()

speakers = {}

entries = []

for child in root:
	if child.tag == "Speakers":
		for x in child:
			the_speaker = x.attrib['id']
			speaker_data = x.attrib
			speakers[the_speaker] = speaker_data
	print type(child)
	if child.tag == "Episode":
		for x in child:
			for y in x:
				# create an entry for each of the turns
				turn_data = {}
				# just copy everything into each entry
				for key in y.keys():
					turn_data[key] = y.attrib[key]
				for z in y:
					print z


input_file.close()