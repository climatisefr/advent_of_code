import sys

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
