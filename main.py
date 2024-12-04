#!/usr/bin/env python3


from importlib import import_module
from sys import argv


def main():
    arg1 = int(argv[1])
    mod = import_module(f"day{arg1}")

    with open(f"test{arg1}.txt") as fin:
        data = []
        for line in fin.readlines():
            data.append(line.strip())
        exp = mod.TEST1
        res = mod.process1(data)
        assert exp == res, f"{exp=} != {res=}"

    with open(f"input{arg1}.txt") as fin:
        data = []
        for line in fin.readlines():
            data.append(line.strip())
        res = mod.process1(data)
        print(res)

    with open(f"test{arg1}.txt") as fin:
        data = []
        for line in fin.readlines():
            data.append(line.strip())
        exp = mod.TEST2
        res = mod.process2(data)
        assert exp == res, f"{exp=} != {res=}"

    with open(f"input{arg1}.txt") as fin:
        data = []
        for line in fin.readlines():
            data.append(line.strip())
        res = mod.process2(data)
        print(res)
        # 553


if __name__ == "__main__":
    main()
