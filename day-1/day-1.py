dial = 50
passwordSum=0

# with open("day-1-example.txt", "r") as file:
#     content = file.read()
with open("day-1-input.txt", "r") as file:
    content = file.read()

commands = content.splitlines()
for command in commands:
    direction = command[0]
    number = int(command[1:])
    if direction == "L":
        dial -= number
        dial = dial % 100
        if dial == 0:
            passwordSum += 1
    elif direction == "R":
        dial += number
        dial = dial % 100
        if dial == 0:
            passwordSum += 1
print(passwordSum)

