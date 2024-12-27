import sys

dir4 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dir4diag = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
dir8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

def readAll(file: str) -> dict:
    """ Read all lines of the input file """
    with open(file, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        return lines

def startTest() -> dict:
    if len(sys.argv) >= 2:
        return readAll(sys.argv[1])
    return dict()

def printD(str):
    if "-d" in sys.argv:
        print(str)

def hasParam(str):
    return str in sys.argv

def getParam(str):
    if not hasParam(str):
        return None
    idx = sys.argv.index(str)
    return sys.argv[idx+1]

def toMap(lines):
    sz = [len(lines[0]), len(lines)]
    map = list()
    for l in lines:
        map.append([x for x in l])
    return [map, sz]

def initMap(sz, val):
    map = list()
    for l in range(sz[1]):
        map.append([val] * sz[0])
    return map

def getAt(map, p, sz):
    if p[0] < 0 or p[1] < 0 or p[0] >= sz[0] or p[1] >= sz[1]:
        return None
    return map[p[1]][p[0]]

def setAt(map, p, sz, val):
    if p[0] < 0 or p[1] < 0 or p[0] >= sz[0] or p[1] >= sz[1]:
        return
    map[p[1]][p[0]] = val

def move(p, d, times=1):
    return [p[0] + d[0] * times, p[1] + d[1] * times]

def add_to_tree(tree, ident, value):
    pos = tree
    for item in ident:
        if item not in pos:
            pos[item] = dict()
        pos = pos[item]
    pos["__END__"] = value

def print_tree(tree, pos, cumul):
    for item in tree:
        if item == "__END__":
            continue
        extra = ""
        if "__END__" in tree[item]:
            extra = " => '" + cumul + item + "'"
        printD("| " * pos + f"* {item} ({len(tree[item].items())}){extra}")
        print_tree(tree[item], pos + 1, cumul + item)

def find_in_tree(tree, ident):
    pos = tree
    for item in ident:
        if item not in pos:
            return None
        pos = pos[item]
    if "__END__" in pos:
        return pos["__END__"]
    return None

