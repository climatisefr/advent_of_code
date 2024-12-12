import starutils


lines = starutils.startTest()
left = []
right = []
for i in lines:
    (l, r) = i.split("   ")
    left.append(int(l))
    right.append(int(r))

print(f"Left {left}")
print(f"Right {right}")

left.sort()
right.sort()

print(f"Left {left}")
print(f"Right {right}")

delta = [ abs(r[0] - r[1]) for r in zip(left, right)]
print(f"Delta: {delta}")
print(f"Sum {sum(delta)}")