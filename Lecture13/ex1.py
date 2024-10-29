#!/usr/bin/python3

input=open('input.txt')
output=open('output.txt','w')
count=0

for sequence in input:
	trimmed=sequence.rstrip()[14:]
	count+=1
	print(f'The length of trimmed sequence {count} is {len(trimmed)}\n')
	output.write(trimmed + '\n')

input.close()
output.close()
