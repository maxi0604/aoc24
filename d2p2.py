import sys
count = 0

def check(nums, k):
    desc, asc = True, True
    skip = False
    for i in range(1, len(nums)):
        prev = nums[i - 1]
        if i == k or (i == 1 and k == 0):
            continue
        elif i == k + 1:
            prev = nums[i - 2]

        if prev > nums[i]:
            asc = False
        elif prev < nums[i]:
            desc = False

        dist = abs(nums[i] - prev)

        if dist < 1 or dist > 3:
            skip = True
            break

    if (desc or asc) and not skip:
        return True
    return False

for line in sys.stdin:
    nums = [int(a) for a in line.split()]
    desc, asc = True, True
    skip = False
    for k in range(-1, len(nums)):
        if check(nums, k):
            count += 1
            break



print(count)

