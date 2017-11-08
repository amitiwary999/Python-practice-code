from collections import Counter, OrderedDict
import itertools
from operator import itemgetter

def count_words(string, n):
    list = string.split(" ")
    a = dict(Counter(list))
    d = sorted(a.items(), key = itemgetter(1), reverse = True)
    for i in range(0, n):
        print(d[i])
    print(d)
    
if __name__ == "__main__":
    count_words("cat bat mat fat rat fat cat bat cat cat", 3)
