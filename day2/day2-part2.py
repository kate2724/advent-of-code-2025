#Now, any number composed of any amount of the same repeating set of numbers
def invalidIDSum(ranges):
    invalidIDSum = 0
    for item in ranges:
        firstNum = int(item.split('-')[0])
        secondNum = int(item.split('-')[1])
        for i in range(firstNum, secondNum +1):
            repeatingNum = False
            stringifiedID = str(i)

            n = len(stringifiedID)
            if n < 2:  # Single-digit numbers are not considered repeating sets
                continue
            # Iterate through possible repeating unit lengths
            for unit_len in range(1, n // 2 + 1):
                if n % unit_len == 0:  # Check if the number length is a multiple of unit_len
                    repeating_unit = stringifiedID[:unit_len]
                    # Construct the expected string by repeating the unit
                    expected_string = repeating_unit * (n // unit_len)
                    if expected_string == stringifiedID:
                        repeatingNum = True
            if repeatingNum:
                invalidIDSum += i
    print(invalidIDSum)
    return invalidIDSum

with open("day2/day2-input.txt", "r") as file:
    content = file.read()
ranges = content.split(',')
invalidIDSum(ranges)

# with open("day2/day2-example.txt", "r") as file:
#     content = file.read()
# ranges = content.split(',')
# invalidIDSum(ranges)

# ranges = ["565653-565659"]
# invalidIDSum(ranges)
