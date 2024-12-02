import sys
count = 0

for line in sys.stdin:
    nums = [int(a) for a in line.split()]
    desc, asc, wrong = 0, 0, 0
    removed = False
    skip = False
    for i in range(1, len(nums)):
        dist = nums[i] - nums[i - 1]

        if dist < 1 or dist > 3:
            wrong += 1

    if (desc + wrong <= 1) or (asc + wrong <= 1):
        count += 1


print(count)

