#!/usr/bin/python3

import re

dna_file=open('long_dna.txt')
dna=dna_file.read()
dna_file.close

#in this exercise, using regex splitting would remove the recognition pattern from fragments, which is not what
#we want and would be especially difficult to compensate for as we add multiple (asymmetric) recognition patterns.
#Would probably be better to use finditer and iteratively slice the sequence at the right indicies directly?

#BpsmI digestion
dig1=re.finditer(r'A[ATCG]TAAT', dna) #can give the location of all BpsmI patterns
slice_ids=[]
for run in dig1:
	slice_ids.append(run.start() + 3)

fragments=[dna]
for i in slice_ids:
	cut_fragment=fragments[-1]
	fragments.pop()
	fragments.append(cut_fragment[:i])
	fragments.append(cut_fragment[i:])
print('Fragments from BpsmI digestion.')
print(fragments)


print('Printing fragment lengths...')
for i in range(len(fragments)):
	print(f'Fragment {i}: {len(fragments[i])} bases long.')
#BpsmI and BpsmII digestion
