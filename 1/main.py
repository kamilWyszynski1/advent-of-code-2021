prev = 0
increases = 0
with open('input.txt') as f:
    lines = f.readlines()
    prev = int(lines[0]) + int(lines[1]) + int(lines[2])
    for inx, line in enumerate(lines[3:]):
        curr = prev - int(lines[inx]) + int(line)
        if curr > prev:
            increases += 1
        prev = curr
        
print(increases)