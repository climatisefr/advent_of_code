import starutils


lines = starutils.startTest()
left = []
right = []
for i in lines:
    (l, r) = i.split("   ")
    left.append(int(l))
    right.append(int(r))

right_map = dict()
for r in right:
    if r in right_map:
        right_map[r] += r
    else:
        right_map[r] = r
print(f"Right_map: {right_map}")
count = 0
for l in left:
    if l in right_map:
        count += right_map[l]
print(f"Count: {count}")