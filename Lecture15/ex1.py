#!/usr/bin/python3
#tests passed
def aminop(protein=str,aa=str):
	'''
	Lecture 15 exercise 1 function. Returns the percentage of a protein sequence an amino acid makes up.
	'''
	percentage=protein.upper().count(aa.upper())/len(protein)*100

	return round(percentage)
