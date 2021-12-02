horizontal, depth, aim = 0, 0, 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        cmd, val  = line.split(' ')
        
        if cmd == 'forward':
            horizontal += int(val)
            depth += aim * int(val)
        elif cmd == 'up':
            aim -= int(val)
        elif cmd == 'down':
            aim += int(val)
print(horizontal * depth)
