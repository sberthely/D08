#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
	for key, value in sorted(h.items()):
		print(key, value)


def print_hist_new(h):
    pass


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
pledge_histogram = {}


def histogram_old(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


def histogram_new(s):
    d = dict()
    for word in s:
        d[word] = 1 + d.get(word, 0)
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    pledge_list = list()
    tmp_lst = list()
    fin = open('pledge.txt', 'r')
    for line in fin:
        tmp_lst = line.strip().split()
        for word in tmp_lst:
            # print(word)
            pledge_list.append(word)
    
    return pledge_list


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    # print_hist_old({'p' : 1, 'a' : 1, 'r' : 2, 'o' : 1, 't' : 1})
    # print_hist_old({'and': 7, 'have': 1, 'people': 1, 'beware': 1, 'am': 1, 'School': 1, 'standards.': 1, 'To': 1, 'design': 2, 'human': 1, 'in': 2, 'technology': 1, 'best': 1, 'needs,': 1, 'what': 1, 'condescending,': 1, 'combat': 1, 'for': 3, 'try:': 1, 'artifacts': 1, 'things': 1, 'create': 2, 'responsible': 1, 'abide': 2, 'defaults.': 1, 'power': 1, 'to': 6, 'mind.': 1, 'technological': 1, 'determinism,': 1, 'world.': 1, 'On': 1, 'honor,': 1, 'do': 1, 'that': 1, 'I': 9, 'serve': 1, 'use': 1, 'important': 1, 'politics,': 1, 'not': 1, 'tussle': 1, 'be': 2, 'with': 1, 'by': 2, 'pledge.': 1, 'ever-mindful': 1, 'remember': 1, 'society,': 1, 'inquisitive': 1, 'technical': 1, 'of': 2, 'privacy': 1, 'will': 5, 'accountable': 1, 'security,': 1, 'the': 5, 'my': 2, 'code.': 1})
    print_hist_old((histogram_new(get_pledge_list())))

    pass

if __name__ == '__main__':
    main()
