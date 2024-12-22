inputValues = input()

n = int(inputValues.split(' ')[0])
m = int(inputValues.split(' ')[1])

list = []
index = 0
count = 1

end = False

for i in range(n):
    list.append(i + 1)

way = str(list[0])

while(not end):
    index += 1
    count += 1

    if index == len(list):
        index = 0

    if list[index] == list[0] and count == m:
        end = True

    if count == m:
        if count == m and index != 0:
            way += str(list[index])
        count = 1

print(way)