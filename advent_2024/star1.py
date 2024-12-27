#!/usr/bin/python3
from starutils import startTest, printD


lines = startTest()
left = []
right = []
for i in lines:
    (l, r) = i.split("   ")
    left.append(int(l))
    right.append(int(r))

printD(f"Left {left}")
printD(f"Right {right}")

left.sort()
right.sort()

printD(f"Left {left}")
printD(f"Right {right}")

delta = [ abs(r[0] - r[1]) for r in zip(left, right)]
printD(f"Delta: {delta}")
print(f"Step 1 sum {sum(delta)}")

right_map = dict()
for r in right:
    if r in right_map:
        right_map[r] += r
    else:
        right_map[r] = r
printD(f"Right_map: {right_map}")
count = 0
for l in left:
    if l in right_map:
        count += right_map[l]
print(f"Step 2 count: {count}")