import heapq
from typing import Optional

class Heap:
    def __init__(self) -> None:
        self.heap = []
        self.count = 0
    
    def push(self, val: str):
        self.heap.append(val)
        self.count += 1

    def pop(self) -> Optional[str]:
        if self.count == 0:
            return None

        self.count -= 1
        el = self.heap[-1]
        self.heap = self.heap[:-1]
        return el


# check_syntax checks if syntax is correct. If not, returned first character that is invalid.
def check_syntax(input: str) -> Optional[str]:
    character_mapping = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>',
    }

    heap = Heap()
    for char in input:
        if char in character_mapping:
            heap.push(character_mapping[char])
        else:
            wanted_character = heap.pop()
            if char == wanted_character:
                continue
            else:
                print(f"Expected {wanted_character}, but found {char} instead")
                return char
    return None

def map_invalid_character(char: Optional[str]) -> int:
    if char is None:
        return 0
    
    return {'}': 1197, ']': 57, ')': 3, '>': 25137}[char]

with open('10/input.txt') as f:
    inputs = [line.strip() for line in f]
    result = 0
    for input in inputs:
        result += map_invalid_character(check_syntax(input))
    print(result)