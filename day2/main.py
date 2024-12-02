#!/usr/bin/env python

from collections import Counter
from itertools import pairwise

def process(fin):
    data = []
    for line in fin.readlines():
        line = line.strip()
        data.append([int(x) for x in line.split(' ') if x])

    safe = 0
    for line in data:
        diff = []
        for x, y in pairwise(line):
            diff.append(x-y)
        pos = all([x > 0 for x in diff])
        neg = all([x < 0 for x in diff])
        gradual = all([abs(x) < 4 for x in diff])
        print(diff, pos, neg, gradual)

        if (pos or neg) and gradual:
            safe += 1

    print(safe)
    return safe

def _safe(line: list) -> bool:
    diff = []
    for x, y in pairwise(line):
        diff.append(x-y)
    pos = all([x > 0 for x in diff])
    neg = all([x < 0 for x in diff])
    gradual = all([abs(x) < 4 for x in diff])
    print(diff, pos, neg, gradual)

    return (pos or neg) and gradual


def process2(fin):
    data = []
    for line in fin.readlines():
        line = line.strip()
        data.append([int(x) for x in line.split(' ') if x])

    safe = 0
    for line in data:
        for x in range(len(line)):
            damped_line = line[:x] + line[x+1:]
            if _safe(damped_line):
                safe += 1
                break
    return safe




def main():
    with open('test.txt') as fin:
        exp = 2
        res = process(fin)
        assert exp == res, f"{exp=} != {res=}"

    with open('input.txt') as fin:
        res = process(fin)
        print(res)
        # 510

    with open('test.txt') as fin:
        exp = 4
        res = process2(fin)
        assert exp == res, f"{exp=} != {res=}"

    with open('input.txt') as fin:
        res = process2(fin)
        print(res)
        # 553



if __name__ == '__main__':
    main()