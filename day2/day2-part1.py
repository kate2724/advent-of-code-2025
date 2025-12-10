
def invalidIDSum(ranges):
    invalidIDSum = 0
    for item in ranges:
        firstNum = int(item.split('-')[0])
        secondNum = int(item.split('-')[1])
        for i in range(firstNum, secondNum +1):
            repeatingNum = False
            stringifiedID = str(i)
            midpoint = len(stringifiedID) // 2
            # Extract the first half using slicing from the start to the midpoint
            first_half = stringifiedID[:midpoint]
            # Extract the second half using slicing from the midpoint to the end
            second_half = stringifiedID[midpoint:]
            if first_half == second_half: #then the number is repeating
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

# ranges = ["11-22"]
# invalidIDSum(ranges)
