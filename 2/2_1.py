horizontal, depth = 0, 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        cmd, val  = line.split(' ')
        
        if cmd == 'forward':
            horizontal += int(val)
        elif cmd == 'up':
            depth -= int(val)
        elif cmd == 'down':
            depth += int(val)
print(horizontal * depth)
