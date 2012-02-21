# file to calc various information theoretic measures

# import nltk... we need it for numerous things here
from nltk import FreqDist
import math

# first get the first file to start with
english_model_name = raw_input("What file has your English model text? ")

english_model = open(english_model_name)
english_model_content = english_model.read()
english_model.close()

#
# First
#
# Here we will determine the relative frequencies of English characters in the text
# Then we will calculate the entropy of the distribution

# here we use the expression list(var_name) to turn our string into a list
# this basically separates each character for us to make it so that it works
# directly in the freqdist function
english_unigram_fdist = FreqDist(list(english_model_content))

english_unigram_entropy = 0.0

# now loop and get the entropy for english unigrams
for unigram in english_unigram_fdist.samples():
    english_unigram_entropy += english_unigram_fdist.freq(unigram) * math.log(english_unigram_fdist.freq(unigram), 2) 

english_unigram_entropy = - english_unigram_entropy

print "The English Unigram Entropy is: " + str(english_unigram_entropy)


#
# Second
#
# Here we will determine the relative frequencies of English bigrams in the text
# Then we will calculate the entropy of the bigram distribution

# create a list to store bigrams in
english_model_bigrams = []

index = 0
english_bigram_fdist = FreqDist()

# we'll be iterating through the string but stop one item short of normal
# this allows us to create bigram windows
while index < (len(english_model_content) -1):
    english_bigram_fdist.inc(english_model_content[index:index+2])
    index += 1


english_bigram_entropy = 0.0

# now loop and get the entropy for english unigrams
for bigram in english_bigram_fdist.samples():
    english_bigram_entropy += english_bigram_fdist.freq(bigram) * math.log(english_bigram_fdist.freq(bigram), 2) 

english_bigram_entropy = - english_bigram_entropy

print "The English Bigram Entropy is: " + str(english_bigram_entropy)


#
# Third
#
# Here we will calculate the conditional entropy of the bigrams based on the unigram condition criteria

english_conditional_entropy = 0.0

# now loop and get the entropy for english unigrams
for bigram in english_bigram_fdist.samples():
    conditional_probability = english_bigram_fdist.freq(bigram) / english_unigram_fdist.freq(bigram[0])
    english_conditional_entropy += english_bigram_fdist.freq(bigram) * math.log(conditional_probability, 2) 

english_conditional_entropy = - english_conditional_entropy

print "The English Conditional Entropy is: " + str(english_conditional_entropy)


#
# Fourth
#
# Here we will calculate the mutual information

english_mutual_information = 0.0

# now loop and get the entropy for english unigrams
for bigram in english_bigram_fdist.samples():
    conditional_probability = english_bigram_fdist.freq(bigram) / (english_unigram_fdist.freq(bigram[0]) * english_unigram_fdist.freq(bigram[1]))
    english_mutual_information += english_bigram_fdist.freq(bigram) * math.log(conditional_probability, 2) 

print "The English Mutual Information is: " + str(english_mutual_information)


#
# Fifth
#
# Here we will calculate that pair which has the highest mutual information

english_highest_mutual_information = 0.0
english_highest_mutual_information_pair = ""

# now loop and get the entropy for english unigrams
for bigram in english_bigram_fdist.samples():
    conditional_probability = english_bigram_fdist.freq(bigram) / (english_unigram_fdist.freq(bigram[0]) * english_unigram_fdist.freq(bigram[1]))
    pmi = math.log(conditional_probability, 2) 
    
    if pmi > english_highest_mutual_information:
        english_highest_mutual_information = pmi
        english_highest_mutual_information_pair = bigram

print "The English Pair with the highest Mutual Information is: " + str(english_highest_mutual_information_pair) + "(" + str(english_highest_mutual_information) + ")"

#
# Sixth
#
# Here we will calculate the cross entropy of the english model and the cleaned english file

english_sample_name = raw_input("What file has your English sample text? ")

english_sample = open(english_sample_name)
english_sample_content = english_sample.read()
english_sample.close()

english_unigram_cross_entropy = 0.0

for character in list(english_sample_content):
    english_unigram_cross_entropy += math.log(english_unigram_fdist.freq(character), 2)

english_unigram_cross_entropy = -(1.0/len(english_sample_content)) * english_unigram_cross_entropy

print "English cross entropy for unigrams: " + str(english_unigram_cross_entropy)

english_bigram_cross_entropy = 0.0

index = 0

english_sample_bigrams = []
while index < len(english_sample_content) -1:
    english_sample_bigrams.append(english_sample_content[index:index+2])    
    index += 1

for bigram in english_sample_bigrams:
    english_bigram_cross_entropy += math.log(english_bigram_fdist.freq(bigram), 2)

english_bigram_cross_entropy = -(1.0/len(english_sample_bigrams)) * english_bigram_cross_entropy

print "English cross entropy for bigrams: " + str(english_bigram_cross_entropy)



#
# Seventh
#
# Here we calculate stuff for Dutch

dutch_model = open("alpina.txt")
dutch_model_content = dutch_model.read()
dutch_model.close()

dutch_unigram_fdist = FreqDist(list(dutch_model_content))

dutch_unigram_entropy = 0.0

# now loop and get the entropy for dutch unigrams
for unigram in dutch_unigram_fdist.samples():
    dutch_unigram_entropy += dutch_unigram_fdist.freq(unigram) * math.log(dutch_unigram_fdist.freq(unigram), 2) 

dutch_unigram_entropy = - dutch_unigram_entropy

print "The Dutch Unigram Entropy is: " + str(dutch_unigram_entropy)


# create a list to store bigrams in
dutch_model_bigrams = []

index = 0
dutch_bigram_fdist = FreqDist()

# we'll be iterating through the string but stop one item short of normal
# this allows us to create bigram windows
while index < (len(dutch_model_content) -1):
    dutch_bigram_fdist.inc(dutch_model_content[index:index+2])
    index += 1


dutch_bigram_entropy = 0.0

# now loop and get the entropy for english unigrams
for bigram in dutch_bigram_fdist.samples():
    dutch_bigram_entropy += dutch_bigram_fdist.freq(bigram) * math.log(dutch_bigram_fdist.freq(bigram), 2) 

dutch_bigram_entropy = - dutch_bigram_entropy

print "The Dutch Bigram Entropy is: " + str(dutch_bigram_entropy)


#
# Eighth  
#
# Here we calculate KL divergence for English and Dutch

unigram_divergence = 0.0

for unigram in dutch_unigram_fdist.samples():
    unigram_divergence += english_unigram_fdist.freq(unigram) * math.log(english_unigram_fdist.freq(unigram) / dutch_unigram_fdist.freq(unigram))

print "KL Divergence for english-dutch unigrams is: " + str(unigram_divergence)

bigram_divergence = 0.0

for bigram in dutch_bigram_fdist.samples():
    if bigram in english_bigram_fdist.samples():
        bigram_divergence += english_bigram_fdist.freq(bigram) * math.log(english_bigram_fdist.freq(bigram) / dutch_bigram_fdist.freq(bigram))

print "KL Divergence for english-dutch bigrams is: " + str(bigram_divergence)


#
# Ninth  
#
# Here we calculate the cross entropy for the english sample with the dutch model

dutch_unigram_cross_entropy = 0.0

for character in list(english_sample_content):
    dutch_unigram_cross_entropy += math.log(dutch_unigram_fdist.freq(character), 2)

dutch_unigram_cross_entropy = -(1.0/len(english_sample_content)) * dutch_unigram_cross_entropy

print "Dutch cross entropy for unigrams: " + str(dutch_unigram_cross_entropy)

dutch_bigram_cross_entropy = 0.0

index = 0

for bigram in english_sample_bigrams:
    dutch_bigram_cross_entropy += math.log(dutch_bigram_fdist.freq(bigram), 2)

dutch_bigram_cross_entropy = -(1.0/len(english_sample_bigrams)) * dutch_bigram_cross_entropy

print "Dutch cross entropy for bigrams: " + str(dutch_bigram_cross_entropy)

