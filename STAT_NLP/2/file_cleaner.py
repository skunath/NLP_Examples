# file cleaner

# importing so we can do regular expression replacing
import re

file_to_clean = raw_input("What file would you like cleaned? ")

# read in the file
cleaning_file = open(file_to_clean)
cleaning_file_text = cleaning_file.read()

# make everything lowercase
cleaning_file_text = cleaning_file_text.lower()

approved_chars = " abcdefghisklmnopqrstuvwxyz"

cleaned_chars_text = ""

index = 0

while index < len(cleaning_file_text):
    if cleaning_file_text[index] in approved_chars:
        cleaned_chars_text += cleaning_file_text[index]

    index += 1


# now we have a string with all the right characters
print cleaned_chars_text

# now we want to remove any additional spaces so that it's only a maximum of one space
cleaned_and_condensed_chars_text = re.sub("\s+", " ", cleaned_chars_text)

print "*" * 50

print "cleaned and condensed:"
print cleaned_and_condensed_chars_text

cleaning_file.close()

output_clean_file = open("clean","w")
output_clean_file.write(cleaned_and_condensed_chars_text)
output_clean_file.close()

