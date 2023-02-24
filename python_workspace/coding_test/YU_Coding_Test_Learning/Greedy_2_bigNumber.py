numData = input()

result = int(numData[0])

for i in range(1, len(numData)):
    num = int(numData[i])

    if num in [0, 1] or result == 0:
        result += num
    else:
        result *= num

print(result)
