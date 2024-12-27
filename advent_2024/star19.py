#!/usr/bin/python3
from starutils import startTest, printD, hasParam, getParam, add_to_tree, find_in_tree, print_tree

lines = startTest()
total = 0

towels = list()
designs = list()

towels = lines[0].split(", ")
designs = lines[2:]

tree = dict()
impossible_tree = dict()
values_tree = dict()

for t in towels:
    add_to_tree(tree, t, 1)

if hasParam("-d"):
    printD(towels)
    print_tree(tree, 0, "")

def possible(str):
    if find_in_tree(impossible_tree, str):
        return False
    if not str:
        return True
    pos = tree
    for idx, c in enumerate(str):
        if c in pos:
            pos = pos[c]
            if "__END__" in pos:
                if possible(str[idx + 1:]):
                    return True
        else:
            add_to_tree(impossible_tree, str, 1)
            return False
    return False

def count(str):
    if find_in_tree(impossible_tree, str):
        return 0
    v = find_in_tree(values_tree, str)
    if v:
        return v

    if not str:
        return 1
    pos = tree
    ret = 0
    for idx, c in enumerate(str):
        if c in pos:
            pos = pos[c]
            if "__END__" in pos:
                ret += count(str[idx + 1:])
        else:
            break
    add_to_tree(values_tree, str, ret)
    return ret

for design in designs:
    if possible(design):
        total += 1
        printD(f"Possible {design}")
    else:
        printD(f"Impossible {design}")

total2 = 0
for design in designs:
    t = count(design)
    printD(f"Count {design} = {t}")
    total2 += t

print(f"Step 1 total: {total}")
print(f"Step 2 total: {total2}")
