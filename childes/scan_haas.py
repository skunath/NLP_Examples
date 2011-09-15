

############################
# Program: scan_haas
# Purpose: The purpose of this program is to demonstrate how to scan a transcript 
# to construct the vocabulary of a child.
#
#
# Date: 9/15/2011
# Author: S. Kunath
############################


####
# Step 1
####

# First we must opend the text file. This is accomplished by the use of open(...)
haas_data = open("./test-haas.txt","r")

####
# Step 2
####

# now we want to scan through each line and print it out
for line in haas_data:
	print line
	
# what we noted here was that it printed out each individual line

####
# Step 3
####
haas_data = open("./test-haas.txt","r")

# now we want to scan through each line and print it out ONLY if it
for line in haas_data:
	if line.split("\t")[1] == "*CHI:":
		print line.strip()
