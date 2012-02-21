# generate a random character sequence

# import necessary random libraries
import random

# create a string to index into for our characters
chars = " abcdefghijklmnopqrstuvwxyz"

length = raw_input("How many characters would you like to randomly produce? ")

# the string we will be constructing
output_string = ""

# an index to keep track of things
index = 0

while index < int(length):
    rand_char = random.randint(0, 26)
    output_string += chars[rand_char]
    index += 1

print "The output string is: "
print output_string


file_out = open("rand_output", "w")
file_out.write(output_string)
file_out.close()
