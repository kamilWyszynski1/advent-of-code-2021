from typing import Dict, List
import math


def increment_in_map(map: Dict, k1: int, k2: int):
    if k1 not in map:
        map[k1] = {}
    if k2 not in map[k1]:
        map[k1][k2] = 0
    map[k1][k2] += 1


class Cords:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __str__(self) -> str:
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

    def calc(self, map: Dict):
        angle = abs(math.degrees(math.atan2(self.y1 - self.y2, self.x1 - self.x2)))

        if angle == 45.0 or angle == 135.0:
            move = [0, 0]
            if self.x1 > self.x2:
                move[0] = -1
            else:
                move[0] = 1
            if self.y1 > self.y2:
                move[1] = -1
            else:
                move[1] = 1

            while self.x1 != self.x2 and self.y1 != self.y2:
                increment_in_map(map, self.x1, self.y1)

                self.x1 += move[0]
                self.y1 += move[1]
            increment_in_map(map, self.x1, self.y1)

            return

        if self.x1 == self.x2:
            # horizontal
            for i in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                if self.x1 not in map:
                    map[self.x1] = {}
                if i not in map[self.x1]:
                    map[self.x1][i] = 0
                map[self.x1][i] += 1
        else:
            # vertical
            for i in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                if i not in map:
                    map[i] = {}
                if self.y1 not in map[i]:
                    map[i][self.y1] = 0
                map[i][self.y1] += 1


def parse(lines: List[str]) -> List[Cords]:
    cords = []
    for line in lines:
        segments = line.replace(" -> ", ",").split(",")
        cords.append(
            Cords(
                int(segments[0]), int(segments[1]), int(segments[2]), int(segments[3])
            )
        )

    return cords


def count_overlaps(map: Dict) -> int:
    count = 0
    for _, v in map.items():
        for _, o in v.items():
            if o >= 2:
                count += 1
    return count


def visualize(map: Dict) -> str:
    mapStr = ""
    for i in range(10):
        for j in range(10):
            added = False
            if j in map:
                if i in map[j]:
                    mapStr += str(map[j][i])
                    added = True
            if not added:
                mapStr += "."
        mapStr += "\n"
    return mapStr


with open("input.txt") as f:
    lines = f.readlines()
    cords = parse(lines)
    map = {}
    for cord in cords:
        cord.calc(map)
    print(count_overlaps(map))
