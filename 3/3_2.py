from typing import List


def comparer(oxygen: bool):
    def cmp(zeros: str, ones: str) -> str:
        if zeros == ones:
            if oxygen:
                return "1"
            return "0"

        if oxygen:
            if ones > zeros:
                return "1"
            return "0"

        if ones > zeros:
            return "0"
        return "1"

    return cmp


def bit_criteria(lines, cmp, inx: int = 0):
    if len(lines) == 1:
        return lines[0]

    m = []

    for line in lines:
        m.append(line[inx])

    most_common = cmp(m.count("0"), m.count("1"))

    new = []
    for line in lines:
        if line[inx] == most_common:
            new.append(line)

    return bit_criteria(new, cmp, inx + 1)


with open("input.txt") as f:
    lines = f.readlines()
    oxy = int(bit_criteria(lines, comparer(True)), 2)
    co2 = int(bit_criteria(lines, comparer(False)), 2)

    print(oxy * co2)
