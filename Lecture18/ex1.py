#!/usr/bin/python3

accs=['xkn59438','yhdck2','eihd39d9','chdsye847','hedle3455','xjhd53e','45da','de37dp']
import re

# contain 5
print('\n#####\nChecking accessions containing 5...')
for acc in accs:
	if re.search(r'5',acc):
		print(acc)
print('\n#####\n')
# contain d or e
print('\nChecking accessions containing d or e...')
for acc in accs:
        if re.search(r'[de]',acc):
                print(acc)
print('\n#####\n')
# contain d and e
print('\nChecking accessions that contain d and e')
for acc in accs:
        if re.search(r'd.*e',acc):
                print(acc)
print('\n#####\n')
# contain d and e with one letter in between
print('\nChecking accessions that contain d and e with one letter in between')
for acc in accs:
        if re.search(r'd\De',acc):
                print(acc)
print('\n#####\n')
# contain d and e in any order
print('\nChecking accessions that contain d and e in any order')
for acc in accs:
        if re.search(r'd',acc) and re.search(r'e',acc):
                print(acc)
print('\n#####\n')
# start with x or y
print('\nChecking accessions that start with x or y')
for acc in accs:
        if re.search(r'^[xy]',acc):
                print(acc)
print('\n#####\n')
# start with x or y and end with e
print('\nChecking accessions that start with x or y and end with e')
for acc in accs:
        if re.search(r'^[xy].*e$',acc):
                print(acc)
print('\n#####\n')
# contains any 3 numbers in any order
print('\nChecking accessions that contains any 3 numbers in any order')
for acc in accs:
        if re.search(r'(\d.*){3,3}',acc): #using findall like below would actually make sure there are only 3 numbers
                print(acc)
print('\n#####\n')
# contains 3 different numbers in the accession
print('\nChecking accessions that contains 3 different numbers in the accession')
for acc in accs:
        numbers=re.findall(r'\d',acc)
        if len(numbers)==3 and len(set(numbers))==3:
                print(acc)
print('\n#####\n')
# contain three or more numbers in a row
print('\nChecking accessions that contain three or more numbers in a row')
for acc in accs:
        if re.search(r'\d{3,}',acc):
                print(acc)
print('\n#####\n')
# end with d followed by either a, r or p
print('\nChecking accessions that end with d followed by either a, r or p')
for acc in accs:
        if re.search(r'd[arp]$',acc):
                print(acc)
print('\n#####\n')
