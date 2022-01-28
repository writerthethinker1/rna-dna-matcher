import string
import os
from time import sleep
import re
from re import search


def clean_genome(genome):

    genome_lines = genome.readlines() # a list of all the lines in the file...

    clean_edits = [] #empty list

    #get rid of any new line characters that make parsing harder...

    iter = len(genome_lines)

    for element in range(0, iter):

        base = genome_lines[element]

        base_edit = base.strip("\n")

        clean_edits.append(base_edit)


    # remove '\n' list entries

    clean_edits = list(filter(None, clean_edits))

    # remove blank spaces between list elements...

    iter2 = len(clean_edits)

    for element in range(0, iter2):

        clean_edits[element] = clean_edits[element].replace(' ', '')


    # join all the genome pieces into one...

    joined_genome = ''.join(str(v) for v in clean_edits) #this is a string of characters all joined together...

    joined_genome = joined_genome.lower() #make lowercase

    # write joined genome with all the letters to a single text file in working directory './'


    return(joined_genome)
