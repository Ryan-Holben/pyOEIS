from urllib2 import urlopen

def search(int_seq):
    search_str = 'http://oeis.org/search?fmt=text&q=' + ','.join([str(i) for i in int_seq])
    print search_str
    results = urlopen(search_str)
    print results
    return results.read()
