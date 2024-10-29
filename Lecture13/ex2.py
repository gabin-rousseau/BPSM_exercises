#!/usr/bin/python3
#open file links and corresponding variables
genomic=open('genomic_dna2.txt').read()
exons_file=open('exons.txt')
exons=[]

sliced=open('genomic_sliced2.txt','w')

#process exons
for line in exons_file:
	exons.append(line.rstrip('\n'))

sliced_cat=''

for exon in exons:
	I=exon.split(',')
	i_start=int(I[0])-1
	i_stop=int(I[1])
	seq=genomic[i_start:i_stop]
	print(f'Concatenating sequence {seq}, from exon with indicies[{i_start}:{i_stop}].')
	sliced_cat += seq

#save concatenated sliced sequence
sliced.write(sliced_cat)

#close all file links
exons_file.close()
sliced.close()



