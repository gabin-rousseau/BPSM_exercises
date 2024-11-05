#!/usr/bin/python3

#tests passed
def aminop(protein:str,aa:list=["A","I","L","M","F","W","Y","V"]):
	'''
	Lecture 15 exercise 2 function. Returns percentage of a protein sequence comprised of
	a list of amino acid residues. Returns by default the percentage of hydrophobic residues.
	'''
	aa_count=0
	for amino in aa:
		aa_count+=protein.upper().count(amino.upper())
	percentage=aa_count/len(protein)*100

	return percentage
