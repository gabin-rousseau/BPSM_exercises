#!/usr/bin/python3

import re

dna_file=open('long_dna.txt')
dna=dna_file.read().rstrip("\n")
dna_file.close

#in this exercise, using regex splitting would remove the recognition pattern from fragments, which is not what
#we want and would be especially difficult to compensate for as we add multiple (asymmetric) recognition patterns.
#Would probably be better to use finditer and iteratively slice the sequence at the right indicies directly?

#BpsmI digestion
print("\n\n Beginning single digestion...")
dig1=re.finditer(r'A[ATCG]TAAT', dna) #can give the location of all BpsmI patterns
slice_ids=[]
for run in dig1:
	slice_ids.append(run.start() + 3)

fragments=[dna]

print(f"\nCut at sites {slice_ids}.\n")

cut_length=0

for i in slice_ids:
	i-=cut_length
	cut_fragment=fragments[-1]
	fragments.pop()
	fragments.append(cut_fragment[:i])
	fragments.append(cut_fragment[i:])
	cut_length+=len(cut_fragment[:i])
print('\nFragments from BpsmI digestion.\n')
print(fragments)


print('Printing fragment lengths...')
for i in range(len(fragments)):
	print(f'Fragment {i}: {len(fragments[i])} bases long.')

#BpsmI and BpsmII digestion
print("\n\nBeginning double digestion...\n")

dig1=re.finditer(r'A[ATCG]TAAT', dna) #can give the location of all BpsmI patterns
dig2=re.finditer(r'GC[AG][AT]TG',dna) #can give location of all BpsmII patterns)

slice_ids=[]

for run in dig1:
        slice_ids.append(run.start() + 3)
for run in dig2:
	slice_ids.append(run.start() + 4) #WARNING: this method assumes
					  #there are no conflicts between digestion sites
					  #(i.e cutting one doesn't disturb another site)

slice_ids.sort()

fragments=[dna]

print(f"\nCut at sites {slice_ids}.\n")

cut_length=0

for i in slice_ids:
        i-=cut_length
        cut_fragment=fragments[-1]
        fragments.pop()
        fragments.append(cut_fragment[:i])
        fragments.append(cut_fragment[i:])
        cut_length+=len(cut_fragment[:i])
print('\nFragments from BpsmI + BpsmII digestion.\n')
print(fragments)


print('Printing fragment lengths...')
for i in range(len(fragments)):
        print(f'Fragment {i}: {len(fragments[i])} bases long.')
