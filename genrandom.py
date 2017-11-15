## genrandom.py
# Forced GC content sequence generator

import os
import sys
import re
import itertools
from random import randint

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation, CompoundLocation
from Bio.Alphabet import IUPAC

def main():
	a = ""
	for i in range(int(sys.argv[1])):
		a = a + str(randint(0, 3))
		
		
	a = re.sub("0", "A", a)
	a = re.sub("1", "C", a)
	a = re.sub("2", "T", a)
	a = re.sub("3", "G", a)

	print a
	
if len(sys.argv) < 2:
    sys.exit("###\n\nUsage: python genrandom.py [LENGTH]]\n\n###")

main()
