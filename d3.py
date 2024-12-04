import re
import sys

instrs = sys.stdin.read()

sum = 0

for a, b in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", instrs):
    a, b = int(a), int(b)
    print(a, b)
    sum += a * b

print(sum)
