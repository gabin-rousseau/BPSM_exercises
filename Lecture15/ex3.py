#!/usr/bin/python3
#tests passed
def basec(dna,threshold=0.5):
	'''
	Lecture 15 exercise 3.
	'''
	undetermined=0
	for base in dna:
		if base.upper() not in 'ATCG':
			undetermined+=1
	proportion=undetermined/len(dna)

	return proportion>threshold
