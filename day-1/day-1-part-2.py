import math

def getPassword(commands):
    dial = 50
    passwordSum = 0
    
    for command in commands:
        direction = command[0]
        number = int(command[1:])
        old_dial = dial
        clicks_at_zero = 0
        if direction == "L":
            # Moving left: count every time we click through position 0
            if dial == 0:
                # Starting at 0, don't count it, but count future passes
                # After leaving 0, we'll hit it again after 100 clicks, then every 100 after that
                if number >= 100:
                    clicks_at_zero = number // 100
                dial = (dial - number) % 100
            else:
                # We'll hit 0 after 'dial' clicks, then every 100 clicks after that
                if number >= dial:
                    # We reach 0 at least once
                    remaining_after_zero = number - dial
                    clicks_at_zero = 1 + (remaining_after_zero // 100)
                dial = (dial - number) % 100
        elif direction == "R":
            # Moving right: count every time we click through position 0
            if dial == 0:
                # Starting at 0, don't count it, but count future passes
                if number >= 100:
                    clicks_at_zero = number // 100
                dial = (dial + number) % 100
            else:
                # We'll hit 0 after (100 - dial) clicks, then every 100 clicks after that
                steps_to_zero = 100 - dial
                if number >= steps_to_zero:
                    # We reach 0 at least once
                    remaining_after_zero = number - steps_to_zero
                    clicks_at_zero = 1 + (remaining_after_zero // 100)
                dial = (dial + number) % 100
        passwordSum += clicks_at_zero
    print(passwordSum)
    return passwordSum

# Test with example first
with open("day-1-example.txt", "r") as file:
    content = file.read()
getPassword(commands = content.splitlines(), debug=True)

with open("day-1-input.txt", "r") as file:
    content = file.read()
commands = content.splitlines()
getPassword(commands=commands)

#All these should give exactly 1

#Basic pass to the left
# getPassword(["L75","R20"])

# #Basic pass to the right
# getPassword(["R75","L20"])
# #Left ending on zero
# getPassword(["L50","R50"])

# getPassword(["L50","L50"])

# #Right ending on zero
# getPassword(["R50","R50"])

# getPassword(["R50","L50"])

# ##All these should give exactly 2

# #Basic pass to the left
# getPassword(["L200"])

# #Basic pass to the right
# getPassword(["R200"])
# #Extra pass Left landing on zero
# getPassword(["L150","L50"])

# getPassword(["L150","R50"])

# # Extra pass Right landing on zero
# getPassword(["R150","L50"])

# getPassword(["R150","R50"])