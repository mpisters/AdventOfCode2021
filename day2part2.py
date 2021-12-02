list = open("day2inputpart2.txt").read().split("\n")
print(list)
aim = 0
horizontal = 0
depth = 0
for i in range(len(list)):
    command = list[i].split(" ")
    if len(command) != 2:
        continue
    direction = command[0]
    move = command[1]
    if direction == "forward":
        horizontal += int(move)
        depth = depth + (aim * int(move))
    if direction == "down":
        aim += int(move)
    if direction == "up":
        aim -= int(move)

print(aim, horizontal, depth, depth * horizontal)
