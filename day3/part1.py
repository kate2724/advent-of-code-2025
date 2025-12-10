
def getJoultage(banks):
    joultagesum = 0
    for bank in banks:
        integer_list = [int(char) for char in bank]
        firstDigit = max(integer_list[:-1])
        newStart = integer_list.index(firstDigit)
        secondDigit = max(integer_list[newStart +1:])
        joultagesum += firstDigit * 10 + secondDigit
    print(joultagesum)
    return joultagesum

# with open("day3/input.txt", "r") as file:
#     content = file.read()

with open("day3/example.txt", "r") as file:
    content = file.read()

with open("day3/input.txt", "r") as file:
    content = file.read()
banks = content.splitlines()
getJoultage(banks)
