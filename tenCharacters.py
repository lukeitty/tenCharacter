#Author: Luke Ittycheria
#Date: 3/1/16
#Program: Ten Characters

f = open("input.txt",'r')
output = open("outputTen.txt",'w')

txtLines = f.readlines()

for line in txtLines:
	output.write(line[:10])
	output.write("\n")
		
f.close()