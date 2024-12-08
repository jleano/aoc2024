TEST1 = 143

TEST2 = 123


def process1(data):
    rules = []
    updates = []

    onrules = True
    for line in data:
        if not line:
            onrules = False
            continue
        if onrules:
            k, v = line.split("|")
            rules.append([int(k), int(v)])
        else:
            updates.append([int(x) for x in line.split(",")])

    res = 0
    for update in updates:
        valid = True
        for k, v in rules:
            before = update.index(k) if k in update else None
            after = update.index(v) if v in update else None
            if before is not None and after is not None and before > after:
                valid = False
                break
        if valid:
            # get middle number
            res += update[int(((len(update) - 1) / 2))]

    return res


def process2(data):
    rules = []
    updates = []

    onrules = True
    for line in data:
        if not line:
            onrules = False
            continue
        if onrules:
            k, v = line.split("|")
            rules.append([int(k), int(v)])
        else:
            updates.append([int(x) for x in line.split(",")])

    res = 0
    tosort = []
    for update in updates:
        for k, v in rules:
            before = update.index(k) if k in update else None
            after = update.index(v) if v in update else None
            if before is not None and after is not None and before > after:
                tosort.append(update)
                break

    for line in tosort:
        newline = sort(line, rules)
        res += newline[int(((len(newline) - 1) / 2))]

    return res


def sort(line, rules):
    for k, v in rules:
        before = line.index(k) if k in line else None
        after = line.index(v) if v in line else None
        if before is not None and after is not None and before > after:
            line[before] = v
            line[after] = k
            return sort(line, rules)
    return line
