# A small program that will read a user specified file and
# produce a list of the rank and frequency of each word


# get input
filename = raw_input("Please specify a file to examine: ")

# open the file
file = open(filename)

# read file contents and assign to a variable
file_string = file.read()

# create a dictionary object to keep track of words
words = {}

# go through every word in the file
for word in file_string.split(" "):
    # see if the dictionary of unique words contains the word
    if not(words.has_key(word)):
        words[word] = 0
    # add 1 to the dictionary for the word
    words[word] = words[word] + 1


# now create another dictionary to sort things by their frequencies
frequencies = {}

for word in words.keys():
    if not(frequencies.has_key(words[word])):
        frequencies[words[word]] = []
    frequencies[words[word]].append(word)

# now spin through and print out the words
rank = 1
freq_list =  sorted(frequencies.keys())
freq_list.reverse()

print "rank\tword\t\tfrequency"
for frequency in freq_list:
    for item in frequencies[frequency]:
        print str(rank) + "\t" + item + "\t\t" + str(words[item])
    rank += 1

