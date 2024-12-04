import re

TEST1 = 161
RES1 = 159892596

TEST2 = 48
RES2 = 92626942


def process1(data):
    regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

    input = "".join(data)

    res = 0
    for match in re.finditer(regex, input):
        first, second = match.groups()
        res += int(first) * int(second)
        print(first, second)
    return res


def process2(data):
    regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))"

    input = "".join(data)

    res = 0
    mul = True
    for match in re.finditer(regex, input):
        first, second, do, dont = match.groups()
        if first and second:
            if mul:
                res += int(first) * int(second)
        else:
            if dont:
                mul = False
            elif do:
                mul = True

    return res
