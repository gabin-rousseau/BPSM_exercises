#!/usr/bin/python3
import re
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Entrez

#1. How many complete COX1 protein records for mammals?
Entrez.email = "s123456@ed.ac.uk"
mysearch = Entrez.esearch(db="protein", term="COX1 Mammalia complete", rettype="count") #make sure to look for appropriate keywords, "Mammal" here would only return below 2000 counts
result = Entrez.read(mysearch)

