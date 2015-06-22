import nltk
import csv
import json
import numpy
from clustering_package import *
from clustering_package.clusterer_classes import *
from nltk.stem.wordnet import WordNetLemmatizer
from Text import Text


class CentroidClusterModule:
	# vocab is default none and will be created from the text if it is
	# None. This is to allow mult-Text vocabs
	utterances = []
	vocab = []

	def __init__(self):
		utterances = []

	def setText(self, aText):
		self.utterances = aText.working_utterances()

	def setVocab(aVocab):
		self.vocab = aVocab

	def createVocabFromText():
		self.vocab = list(set([word for sublist in self.utterances for word in sublist]))
	# getTags is the big one in Modules. It returns a list that is as long as its uttereances
	# with whatever tags were applied  to them. They are returned as  dictionary in which
	# the key is the tagname, and the value is a sorted list of the tag value for each utterance

	# getTags will take different numbers of parameters, but ALWAYS a tag_name. Or what? Maybe not...
	def getTags(tag_name, num_clusters):
        # frist vectorize the utterances
		f = lambda x : [x.count(word) for word in vocab]
		vectorized_utterances = [f(utterance) for utterance in utterances]
		f = lambda x: x if numpy.dot(x, x) == 0 else x / numpy.sqrt(numpy.dot(x, x))
		norm_vecs = [f(x) for x in vectorized_utterances]
		# orthoganolize them
		orthogonalized = [orthogonalize(x) for x in norm_vecs]
		# create the clusterer 
		clusterer = CentroidClusterer(vector_names = range(len(utterances)), normalise = False)
		clusterer.cluster(vectors, trace = True)
		clustered_names = clusterer._name_dendogram.groups(3)


def orthogonalize(doc_vectors):
        total_v = doc_vectors[0]
        for vector in doc_vectors[1:]:
                total_v = total_v + vector
        total_v = norm_vec(total_v)
        new_doc_vectors = []
        for vector in doc_vectors:
            new_vector = norm_vec(vector - numpy.dot(vector, total_v) * total_v)
            new_doc_vectors = new_doc_vectors + [new_vector]
        return new_doc_vectors


def norm_vec(vec):
    mag = numpy.dot(vec, vec)
    if mag == 0:
        return vec
    else:
        return(vec / numpy.sqrt(mag))

def vectorize_question(utterances):
    vocab = clean_vocabulary(a_questionnaire)
    entries = get_entries(a_questionnaire)
    the_vectors = {}
    for name in entries.keys():
        the_vectors[name] = [entries[name].count(word) for word in vocab]
    return the_vectors