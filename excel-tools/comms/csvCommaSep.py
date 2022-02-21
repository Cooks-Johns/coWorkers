import collections
import csv

def counter(r):
    return collections.Counter(r)


def reader(file):
    with open(file, 'r') as csvfile:
        count_str = csv.reader(csvfile, delimiter=',')

        for row in count_str:
            r = row

    freq = counter(r)

    for (key, value) in freq.items():
        print(key, value)


reader(file='input1.csv') # Make this a input so
