from nltk.corpus import wordnet
syns = wordnet.synsets("program")
print "All Syns"
print(syns)

print "\n\n\n To print a specific Sync"
print(syns[0].name())

print "\n\n\n To print a specific Sync Name (Word)"
print(syns[0].lemmas()[0].name())

print "\n\n\n To print a specific Sync Defination (Word)"
print(syns[0].definition())


print "\n\n\n To print a specific Sync Example (Word)"
print(syns[0].examples())
