# -*- coding: utf-8 -*-
from urllib2 import urlopen

test_data_three_results = open('test_data_three_results.txt', 'rb').read()
test_data_by_id = open('test_data_by_id.txt', 'rb').read()


def search(int_seq):
    search_str = 'http://oeis.org/search?fmt=text&q=' + ','.join([str(i) for i in int_seq])

    # # results = urlopen(search_str).read().split('\n')
    lines = test_data_three_results.split('\n')
    ids = get_seq_ids(lines)
    for id_ in ids:
        print get_known_seq_elements(lines, id_), '\n'
    

# Internal library functions follow:

def get_known_seq_elements(lines, seq_id):
    S = find_entry(lines, 'S', seq_id)
    T = find_entry(lines, 'T', seq_id)
    U = find_entry(lines, 'U', seq_id)

    if S:
        S = [int(x) for x in S[0].split(',')[:-1]]
    if T:
        T = [int(x) for x in T[0].split(',')[:-1]]
    if U:
        U = [int(x) for x in U[0].split(',')[:-1]]

    seq = S + T + U
    return seq

def find_entry(lines, entry_code, seq_id = None):
    results = []
    if seq_id != None:
        for l in lines:
            if l[0:10] == '%' + entry_code + ' ' + seq_id:
                results.append( l[11:] )
    else:
        results = []
        for l in lines:
            if l[0:2] == '%' + entry_code:
                results.append( l[3:] )

    return results

def get_seq_ids(lines):
    results = find_entry(lines, 'I')
    return [x[:7] for x in results]
