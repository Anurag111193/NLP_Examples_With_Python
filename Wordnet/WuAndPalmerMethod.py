from nltk.corpus import wordnet

print "To print  Wu and Palmer method"

print "Comparision of Ship and Boat"

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

print "Comparision of ship and car"

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))


print "Comparision od ship and cat"

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))
