print("file path:")
filePath = input()

with open(filePath, 'r') as f:
    values = f.read().splitlines()

result = None
for i in values:
    minValue = 0
    for j in values:
        if int(j) > int(i):
            minValue += int(j) - int(i)
        elif int(j) < int(i):
            minValue += int(i) - int(j)
    if result is None or result > minValue:
        result = minValue

print(result)