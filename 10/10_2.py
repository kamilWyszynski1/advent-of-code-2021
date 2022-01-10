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
    
    def len(self) -> int:
        return self.count


# check_syntax checks if syntax is correct. If not, returned first character that is invalid.
def check_syntax_with_missing(line:int, input: str) -> Optional[str]:
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
                return None
    
    missing_characters = ''
    # probalby incomplete.
    while heap.len() != 0 :
        missing_characters += heap.pop()
    
    print(f"Complete line {line} by adding {missing_characters}") 
    return missing_characters

def map_missing_characters_value(missing: str) -> int:
    if missing == '' or missing == None:
        return 0

    score = {'}': 3, ']': 2, ')': 1, '>': 4}
    sum = 0
    for char in missing:
        sum *= 5
        sum += score[char]

    print(f"Missing characters {missing} has value {sum}")
    return sum

with open('10/input.txt') as f:
    inputs = [line.strip() for line in f]
    results = []
    for i, input in enumerate(inputs):
        score = map_missing_characters_value(check_syntax_with_missing(i, input))
        if score == 0:
            continue
        results.append(score)
    
    results.sort()
    print(results[len(results)//2])