import sys


sum = 0
rules = []
for line in sys.stdin:
    if "|" in line:
        a, b = line.split("|")
        rules.append((int(a), int(b)))
    else:
        if line == "\n":
            continue
        order = [int(i) for i in line.split(",")]
        valid = True

        for idx, i in enumerate(order):
            for j in order[idx:]:
                for a, b in rules:
                    if i == b and j == a:
                        valid = False
                        break

        if valid:
            continue
        else:
            updated = True
            while updated:
                updated = False
                for f in range(len(order)):
                    for g in range(f, len(order)):
                        va= order[f]
                        vb = order[g]

                        for r, s in rules:
                            if va == s and vb == r:
                                order[f], order[g] = order[g], order[f]
                                updated = True
                                break

            print(order)
            sum += order[len(order)//2]

print(sum)
