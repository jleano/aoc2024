#!/usr/bin/env python

from collections import defaultdict

def process(fin):
    data = []
    for line in fin.readlines():
        line = line.strip()
        data.append([int(x) for x in line.split(' ') if x])
    first = sorted([x[0] for x in data])
    second = sorted([x[1] for x in data])
    pairs = zip(first, second)

    ret = 0
    for (v1, v2) in pairs:
        ret += abs(v1 - v2)
    return ret


def process2(fin):
    data = []
    for line in fin.readlines():
        line = line.strip()
        data.append([int(x) for x in line.split(' ') if x])
    
    num_of_times = defaultdict(lambda: 0)
    for x in data:
        num_of_times[x[1]] += 1
    
    res = 0
    for x in data:
        res += x[0] * num_of_times[x[0]]
    return res


def main():
    with open('test.txt') as fin:
        exp = 11
        res = process(fin)
        assert exp == res, f"{exp=} != {res=}"

    with open('input.txt') as fin:
        res = process(fin)
        print(res)
        # 1319616

    with open('test.txt') as fin:
        exp = 31
        res = process2(fin)
        assert exp == res, f"{exp=} != {res=}"

    with open('input.txt') as fin:
        res = process2(fin)
        print(res)
        # 27267728



if __name__ == '__main__':
    main()