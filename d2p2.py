import sys




def check_asc(nums):
    wrong = 0
    skip = False
    for i in range(1, len(nums)):
        if skip:
            skip = False
            continue
        diff = nums[i] - nums[i - 1]
        if not 1 <= diff <= 3:
            wrong += 1

    return wrong <= 1


def check_desc(nums):
    wrong = 0
    skip = False
    for i in range(1, len(nums)):
        if skip:
            skip = False
            continue
        diff = nums[i] - nums[i - 1]
        if not -3 <= diff <= -1:
            wrong += 1

    return wrong <= 1



n = 0
for i, line in enumerate(sys.stdin):
    nums = [int(a) for a in line.split()]
    if check_asc(nums) or check_desc(nums):
        n += 1
        # print(i)

print(n)

