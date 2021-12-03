m = {}
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        for inx, c in enumerate(line):
            if c != "\n":
                if inx not in m:
                    m[inx] = {}
                if c not in m[inx]:
                    m[inx][c] = 0
                m[inx][c] += 1

gamma = ""
epsilon = ""
for k, v in m.items():
    if v["0"] > v["1"]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gammaInt = int(gamma, 2)
epsilonInt = int(epsilon, 2)

print(gammaInt * epsilonInt)
