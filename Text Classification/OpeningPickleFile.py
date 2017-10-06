import nltk
import pickle

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
print "File Loaded"
classifier_f.close()

print "File Closed"
