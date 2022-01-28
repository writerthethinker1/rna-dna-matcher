## RNA-DNA Matcher!

This is the RNA-DNA sequence matcher! It features colored terminal prompts, easy to read dialogue, text files for comparisons, more memory deallocation, knowledge of how much memory the program used and explanations about how to interpret your findings once you examine for any matches.

To use this package, please make sure you have the packages:

* colorama
* string
* os
* time
* re
* itertools
* gc
* psutil

installed via `pip install [package name]`

For the best results, try longer chains of splice lengths, the program is ideal for longer chains of rna or dna sequences.

### Using it

To use the package once you have the basics installed, simply run

> python3 sequence-matcher.py

inside the *rna-dna-matcher* directory and follow the prompts!

This package comes with a *genomes* folder where you can put your genomes as strings in '.txt' format for analysis later with the sequence-matcher.py. Included are dummy examples of 'polio' and 'ebola' genomes. They aren't real! They are just there for illustration. You put your own genomes to test out there; they just have to be text file format, a string basically.

### Giving a test run

To see if you have things working, try using the genomes given with splice length '40', the suspect as *polio*, virus as *ebola* and *accept filtering* to find 2 pairs of numbers for matches. If you output:

> ['[223, 275]', '[107, 149]']

in either order, you have the matcher working and can match more genomes! The numbers given between the quotes are the character numbers in the *suspect* file. The string there is also inside the original virus file. Just use a search filter on your text editor with this string to locate where the match is in the original virus file. Instructions are also given when you run the code. 

Congrats! You're all set for analysis! Enjoy!
