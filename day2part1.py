list = open("day2inputpart1.txt").read().split("\n")
print(list)
depth = 0
horizontal = 0
for i in range(len(list)):
    command = list[i].split(" ")
    if len(command) != 2:
        continue
    direction = command[0]
    move = command[1]
    if direction == "forward":
        horizontal += int(move)
    if direction == "down":
        depth += int(move)
    if direction == "up":
        depth -= int(move)

print(depth, horizontal, depth * horizontal)
