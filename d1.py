import sys
left, right = [], []

for line in sys.stdin:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

print("p1: ", sum([abs(x - y) for (x, y) in zip(left, right)]))
print("p2: ", sum([i * right.count(i) for i in left]))
