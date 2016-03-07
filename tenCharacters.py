#Author: Luke Ittycheria
#Date: 3/1/16
#Program: Ten Characters

f = open("input.txt",'r')#Open the input file
output = open("outputTen.txt",'w')#Open the output file

txtLines = f.readlines() #Read the text

for line in txtLines:
	output.write(line[:10])#Write the new lines of code to the output file
	output.write("\n")
		
f.close()#close file
