import re
import sys

instrs = sys.stdin.read()

sum = 0

replaced = re.sub(r"don't\(\).*?(do\(\)|$)", "", instrs, flags = re.DOTALL)

for a, b in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", replaced):
    a, b = int(a), int(b)
    print(a, b)
    sum += a * b

print(sum)
