# here to see various sequences in snake order 1 2 3 4 5 | 2 3 4 5 6 | 3 4 5 6 7 and so on...
#then...detect spliced rna or just sequence matches...
#om a ra pa tsa na dhi
# author: ramneek narayan

#input: text file of genome
#output: vector of sequences, matches, dialogue if so or not...

import string
import os, psutil, gc, time
from time import sleep
import re
from re import search
from filter import my_filter
from itertools import chain
from clean_genomes import clean_genome
import colorama
from colorama import Fore, Back, Style
import colors

file_path = input("enter the" + colors.cyan("suspect genome") + "file location: ") #write the file path before using program. e.g. ~/Docs/genome.txt

#error handling for typos in file path...
while os.path.exists(file_path) == False:
    file_path = input("file not found, try again: ")

suspect_genome = open(file_path,"r")

suspect_genome = clean_genome(suspect_genome)
# now we extract all the sequences for a determined length...

splice_length = input("what is the" + colors.cyan("splice") + "length?: ")

while splice_length.isdigit() == False or int(splice_length) > len(suspect_genome):
    splice_length = input("typo, enter only integers: ")

print("generating sequence partitions...")

splice_length = int(splice_length)

nucleotide_count = len(suspect_genome) #number of nucleotides...

# use a iterator to extract all sequences, sliding style...

item = 0

segments_rna = []

if (item + splice_length) == nucleotide_count:
    segments_rna = segments_rna.append(str(suspect_genome)) #this is more robust, can also check rna of vaccines with past viral infections

else:

    while (item + splice_length) <= nucleotide_count:

        #iterate over the segments...

        sequence = suspect_genome[item:(item + splice_length)]

        #store into segments_rna list:

        segments_rna.append(sequence)

        item += 1 #increment next count

# get rid of repeat elements in list...

# now we check the actual genome...

true_genome = input("file path of the" + colors.cyan("virus genome") + "you wish to check for spliced code?: ")

while os.path.exists(file_path) == False:
    file_path = input("file not found, try again: ")

check_genome = open(true_genome,"r")

check_genome = clean_genome(check_genome) #a string of genome we wish to check

# check elements of spliced_rna against check_genome:
sleep(1)
print("searching...")

match_list = []

for segment_pos in range(0, len(segments_rna)):

    check_res = search(segments_rna[segment_pos], check_genome)

    match_list.append(check_res)


# from match list, extract tuples of positions, removing 'None' and marking spans...


#now get rid of empty elements...

positions = list(filter(None, match_list))

#now get the tuples for character positions...

for item in range(0, len(positions)):

    positions[item] = re.findall(r'\(.+?\)', str(positions[item]))


# check if there are any matches...

if positions != []:

    pattern_matches = len(positions)

    sleep(2)
    print("done! " + colors.cyan(str(pattern_matches)) + " matches for a " + colors.cyan(str(splice_length)) + " splice length found!")

    #ask for filtered results (too many matches on terminal)

    sleep(1)
    print("would you like" + colors.cyan("filtered results") + "for consequtive matches?")
    sleep(1)
    print("if the match is longer than " + colors.cyan(str(splice_length)) + " it can be condensed...")
    ask_filter = input("...the result would be (a, b), (a + 1, b + 1) -> (a, b + 1): ")

    while ask_filter != 'yes' and ask_filter != 'y' and ask_filter != 'n' and ask_filter != 'no':
        ask_filter = input("yes or no only, please: ")

    if (ask_filter == 'yes' or ask_filter == 'y'):
        sleep(0.5)
        print("filtering...")
        if (pattern_matches > 1):
            my_filter(positions)
        else:
            print(colors.cyan(positions))

    elif (ask_filter == 'no' or ask_filter == 'n'):
        sleep(0.5)
        print("won't display filtered results...")

        all_results = input("would you like to see all of the raw unfiltered matches instead?: ")

        while all_results != 'yes' and all_results != 'y' and all_results != 'n' and all_results != 'no':
            all_results = input("yes or no only, please: ")

        if (all_results == 'yes' or all_results == 'y'):
            sleep(0.5)
            print("here are all the raw, unfiltered matches...")
            print(colors.cyan(list(chain(*positions))))

        else:
            print("won't show any matches...")

    # tell how to check...
    sleep(1)
    need_check = input("would you like to know how to check this result?: ")
    while need_check != 'yes' and need_check != 'y' and need_check != 'n' and need_check != 'no':
        need_check = input("yes or no only, please: ")

    if (need_check == 'yes' or need_check == 'y'):
        print("to check, go to the" + colors.cyan("virus file") + "and check the character positions given for the string...")
        sleep(0.5)
        print("the numbering given here means the" + colors.cyan("beginning character") + "in the genome is counted as" + colors.cyan("'0'..."))
        sleep(1)
        print("when in doubt," + colors.cyan("add 1 to both numbers in that are paired and search!"))
        sleep(1)
        print("the pairs mean" + colors.cyan("'from character X to Y'"))
        sleep(1)
        print("from there you can find the same string inside the" + colors.cyan("suspect..."))
        sleep(1)
        print("they share the same genetic code!")
        sleep(0.5)

    # now output filtered text files to user if they ask...

    # two genomes are suspect_genome and check_genome

    sus_print = input("would you like the cleaned genome for the" + colors.cyan("suspect") +  "saved?: ")

    while sus_print != 'yes' and sus_print != 'y' and sus_print != 'n' and sus_print != 'no':
        sus_print = input("yes or no only, please: ")

    sleep(0.3)
    check_print = input("would you also like the cleaned genome for the" + colors.cyan("virus") + "saved?: ")

    while check_print != 'yes' and check_print != 'y' and check_print != 'n' and check_print != 'no':
        check_print = input("yes or no only, please: ")


    if sus_print == 'yes' or sus_print == 'y':

        sleep(0.5)
        golden_suspect_name = input("what's the file name you want for the cleaned suspect genome?: ")
        #save to .txt extension

        golden_sus_genome = open(golden_suspect_name, "w")

        golden_sus_genome.write(suspect_genome)
        golden_sus_genome.close()
        sleep(1)
        print("saved! check ./" + str(golden_suspect_name) + " to see genome.")
        sleep(0.5)


    if check_print == 'yes' or check_print == 'y':

        sleep(0.5)
        golden_virus_name = input("what's the file name you want for the cleaned virus genome?: ")
        #save to .txt extension.

        golden_virus_genome = open(golden_virus_name, "w")

        golden_virus_genome.write(check_genome)
        golden_virus_genome.close()
        sleep(1)
        print("saved! check ./" + str(golden_virus_name) + " to see genome.")
        sleep(0.5)


    if check_print == 'yes' or check_print == 'y' or sus_print == 'yes' or sus_print == 'y':

        print("happy character inspection!")

#case no matches at all
else:
    sleep(2)
    print("there were no matches for " + colors.cyan(str(splice_length)) + " splice length.")

gc.collect() #remove memory by end of program...

# print(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2) + "MB memory used...") #get memory usage
