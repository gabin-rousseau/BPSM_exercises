#!/usr/bin/python3

import os
import sys
import subprocess

#store the two sequences in string variables
genomic=open("plain_genomic_seq.txt").read().upper().replace("\n","")
remote=open("remote.fa").read().upper().replace("\n","")

#define the DNA string checker function, returns a boolean value and.
def check(test_str):
	import re
	report=False
	#http://docs.python.org/library/re.html
	#re.search returns None if no position in the string matches the pattern
	#pattern to search for any character other then . a-z 0-9
	pattern = r'[^ACGTUWSMKRYBDHVN-]' #pattern matching to detect sequences that don't match DNA syntax.
	if re.search(pattern, test_str):
		#Character other then ATCG was found
		#print('Invalid : %r' % (test_str,))
		report=False
	else:
		#No character other then ATCG  was found
		#print('Valid   : %r' % (test_str,))
		report=True
	return report

#slice the local sequence based on reported coding/non-coding sequences
genomic_CDS1=genomic[:63]
genomic_NCDS=genomic[63:90]
genomic_CDS2=genomic[90:]

#same with the remote sequence
remote_NCDS1=remote[0:28]
remote_CDS=remote[28:409]
remote_NCDS2=remote[409:]

print(f"Local sequence is DNA: {check(genomic)}") #is the local sequence DNA? Report and store in a boolean variable
genomic_DNA=check(genomic)
print(f"Remote sequence is DNA: {check(remote)}") #same with the remote sequence
remote_DNA=check(remote)










