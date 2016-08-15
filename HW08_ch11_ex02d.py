#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict()
    for key, value in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = dict()
    for key, value in d.iteritems():
        inverse[value] = inverse.get(value, [])
        inverse[value].append(key)

    # If the element where unique, the following line could have worked
    # inverse = {v: k for k, v in d.items()}

    return inverse


def print_hist_newest(d):
    count = 0
    for key, value in sorted(d.items()):
        count += 1
        if count != int(key):
            while count < int(key):
                print('{}: {}'.format(count, ''))
                count += 1
        print('{}: {}'.format(key, value))

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
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
