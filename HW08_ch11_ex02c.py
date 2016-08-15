#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports

# Body
def reverse_lookup_old(d, v):
	tmp_list = list()
	for k in d:
		try:
			if str(d[k]) == v:
				tmp_list.append(k)
		except:
			raise ValueError
	return tmp_list


def reverse_lookup_new(d, v):
	tmp_list = list()
	for k in d:
		try:
			if str(d[k]) == v:
				tmp_list.append(k)
		except:
			raise ValueError
	return tmp_list


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
def main():   # DO NOT CHANGE BELOW
    # print(reverse_lookup_old(pledge_histogram, "1"))
    # print(reverse_lookup_old(pledge_histogram, "9"))
    # print(reverse_lookup_old(pledge_histogram, "Python"))
    # print(reverse_lookup_old(pledge_histogram, "7"))

    print(reverse_lookup_new(histogram_new(get_pledge_list()), "1"))
    print(reverse_lookup_new(histogram_new(get_pledge_list()), "9"))
    print(reverse_lookup_new(histogram_new(get_pledge_list()), "Python"))
    print(reverse_lookup_new(histogram_new(get_pledge_list()), "7"))


if __name__ == '__main__':
    main()
