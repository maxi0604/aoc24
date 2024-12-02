import sys
count = 0

for line in sys.stdin:
    nums = [int(a) for a in line.split()]
    desc, asc = True, True
    skip = False
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            asc = False
        elif nums[i - 1] < nums[i]:
            desc = False

        dist = abs(nums[i] - nums[i - 1])

        if dist < 1 or dist > 3:
            skip = True
            break

    if (desc or asc) and not skip:
        count += 1


print(count)

