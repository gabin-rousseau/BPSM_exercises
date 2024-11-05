#!/usr/bin/python3

def kmerc(dna:str, k:int=2, n:int=2):
	'''
	Lecture 15 exercise 4.
	'''
	from collections import Counter
	k_mers=[]

	for i in range(len(dna)-k+1):
		k_mers.append(dna[i:i+k])

	k_counts=Counter(k_mers)

	for key in k_counts.keys():
		if k_counts[key]>n:
			print(f"{k}-mer {key} occurs more than {n} time(s).")

