#aims to condense certain tuples in lists...
#om a ra pa tsa na dhi
#input: list of the form: ['(1, 100)', '(2, 101)', '(3, 102)', ..., '(9, 1000)']
#output: condensed list of the form: ['(1, 102)', '(9,1000)']

import re
from re import search
from itertools import chain
from time import sleep
import colors

def my_filter(test): #test is a list of matches from sequence-matcher.py

    #test = [['(511, 561)'], ['(512, 562)'], ['(513, 563)'], ['(514, 564)'], ['(515, 565)'], ['(516, 566)'], ['(517, 567)'], ['(518, 568)'], ['(519, 569)'], ['(520, 570)'], ['(521, 571)'], ['(522, 572)'], ['(523, 573)'], ['(524, 574)'], ['(525, 575)'], ['(526, 576)'], ['(530, 580)'], ['(534, 584)'], ['(535, 585)'], ['(536, 586)'], ['(537, 587)'], ['(538, 588)'], ['(539, 589)'], ['(540, 590)'], ['(541, 591)'], ['(542, 592)'], ['(543, 593)'], ['(789, 839)'], ['(790, 840)'], ['(791, 841)'], ['(792, 842)'], ['(793, 843)'], ['(794, 844)'], ['(795, 845)'], ['(796, 846)'], ['(797, 847)'], ['(798, 848)'], ['(799, 849)'], ['(800, 850)'], ['(801, 851)'], ['(802, 852)'], ['(803, 853)'], ['(804, 854)'], ['(805, 855)'], ['(806, 856)'], ['(807, 857)'], ['(808, 858)'], ['(809, 859)'], ['(810, 860)'], ['(811, 861)'], ['(812, 862)'], ['(813, 863)'], ['(814, 864)'], ['(815, 865)'], ['(816, 866)'], ['(817, 867)'], ['(818, 868)'], ['(819, 869)'], ['(820, 870)'], ['(821, 871)'], ['(822, 872)'], ['(823, 873)'], ['(824, 874)'], ['(825, 875)'], ['(826, 876)'], ['(827, 877)'], ['(828, 878)'], ['(829, 879)'], ['(830, 880)'], ['(831, 881)'], ['(832, 882)'], ['(833, 883)'], ['(834, 884)'], ['(835, 885)'], ['(836, 886)'], ['(837, 887)'], ['(838, 888)'], ['(839, 889)'], ['(840, 890)'], ['(841, 891)'], ['(842, 892)'], ['(843, 893)'], ['(844, 894)'], ['(845, 895)'], ['(846, 896)'], ['(847, 897)'], ['(848, 898)'], ['(849, 899)'], ['(850, 900)'], ['(851, 901)'], ['(852, 902)'], ['(853, 903)'], ['(854, 904)'], ['(855, 905)'], ['(856, 906)'], ['(857, 907)'], ['(99999,9999999)'], ['(1000000, 100000000)'], ['(1000001, 100000001)']] #you can test the function using this sequence...

    test = list(chain(*test)) #unlisting nested lists...

    test.append(test[len(test)- 1]) #making the end entry a duplicate of the last one
    #to force a mismatch on purpose...for counting later

    condensed = [] #condensed list, take only the first element in the tuple (a,b): extract a

    #ex: condensed = [1, 2, 3, 4, 5] or [a, b, c, d, e] for any (real) numbers a-e

    #first condense the list to first entries only...

    iter = len(test)

    #start iterating the list

    #method:
    # extract the first entry in the tuple character: (9, 100) -> '9' and append to condensed
    #end with a list like [1, 2, 3, 4]

    for item in range(0, iter):

        trimed = str(re.findall(r'\([0-9]+',str(test[item])))
        trimed = re.findall(r'[0-9]+', trimed)
        condensed.append(int(trimed[0]))



    # next we see how long consecutive numbers are...
    # input: [1, 2, 3, 4, 5, 9, 10, 11, 12, 13], then
    # maybe 1 2 3 4 5 6 7 | 200 201 202 | 300 301 302 303 304 305 | 323 324 325 326 327 328 329
    # we record indicies: 0+4, 5+9

    bool = [1] #list of matches


    #making a simple boolean list of consecutive matches or not, 0 means no and 1 means yes
    #idea is that numbers that match have a difference of 1
    for item in range(0, iter - 1):

        if (condensed[(item + 1)] - condensed[item] == 1):
            bool.append(1)
        else:
            bool.append(0)

    index = [1] #initialize with 1 for extra element

    #making a simple index recorder of the items that do match, when
    #the sum is on between consecutive list elements, we mark the either the beginning or the
    #end of the pairs that can be joined... pattern: 0 1 (beg) or 1 0 (end)
    for item_location in range(0, iter - 1):

        if (bool[item_location] + bool[item_location + 1] == 1):

            index.append(item_location + 1)
        else:
            continue

    #editing it for the indicies to use later, e.g. sequence at 11 can be joined with that in 12
    #(slide by 1 letter)
    index[:] = [x - 1 for x in index]
    #print(index)

    #index also can't have repeat elements in beginning
    if (index[0] == index[1]):
        index = index[2:]


    #print(index)
    #extract essential items from test:

    essential = []

    for item in range(0, len(index)):

        essential.append(test[index[item]]) #this will be the character lengths that can be condensed
        #there are consecutive matches here... read by each two elements, from element 1 to 2 it can
        #be condensed by consecutive matches


    #now get all unique entries...with no adjoining possible...
    #this imples a sequence like 1 2 3 4 |200| 300 301 302 |400| |450| 500 501 502...
    #200, 400, 450 are what we are trying to find

    #put the condensed matches together in a tuple form: (300,400) for (300, 350), (360, 400)
    #...

    #remove last element we added...

    del test[(len(test) - 1)]

    #first make tuples of list indices

    del condensed[len(condensed) - 1] #remove extra element we added to condensed

    # now have in easy format...

    first_char = [] #list of all of the first character positions in condensed

    for item in range(0, len(essential), 2):

        trimed = str(re.findall(r'\([0-9]+',str(essential[item])))
        trimed = re.findall(r'[0-9]+', trimed)
        first_char.append(int(trimed[0]))

    last_char = [] #list of all of the first character positions in condensed

    for item in range(1, len(essential), 2):

        trimed = str(re.findall(r'[0-9]+\)',str(essential[item])))
        trimed = re.findall(r'[0-9]+', trimed)
        last_char.append(int(trimed[0]))

    #now put the chars in coordinate form:

    for iterator in range(0, len(last_char)):

        last_char[iterator] = str([first_char[iterator], last_char[iterator]])

    #now give user dialogue about the ends that can be joined together...

    print("there were some matches that were consecutive...")
    sleep(1)
    print("we give the beginning of the match to the end of the last one...")
    print("[first character, last character]")

    print(colors.cyan(list(set(last_char))))



    ########no matches part

    no_match = [] #a list of items that can't be matched, positions of the no match #note: order does not matter

    if (condensed[1] - condensed[0] != 1): #check if beginning has consecutive numbers, if not, no match
        no_match.append(0)

    if (condensed[len(condensed) - 1] - condensed[len(condensed) - 2] != 1):
        #check if end has consecutive numbers, if no, no match
        no_match.append(len(condensed) - 1)

    for pos in range(1, len(condensed) - 1):
        #check if middle entries are consecutive or not, if no, no match, always will have pattern
        # 1 0 0 1

        if (condensed[pos + 1] - condensed[pos] != 1 and condensed[pos] - condensed[pos - 1] != 1):
             no_match.append(pos)


    non_slide = []

    # get the non-matching character positions
    for pos2 in range(0, len(no_match)):

        non_slide.append(test[no_match[pos2]])

    # give the results...

    if (len(non_slide) > 0):

        sleep(2)
        print("matches that can't share the same parts are given by the character positions...")
        print(colors.cyan(list(set(non_slide))))
    else:

        print("there were no matches that were of the sequence length only once.")

# let's test it out
