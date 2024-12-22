import math

def Formula(dotX, dotY, circleX, circleY):
    return math.sqrt(((dotX - circleX) ** 2) + ((dotY - circleY) ** 2))


with open('circle.txt', 'r') as f:
    circleCoordinates = f.read().splitlines()

circleX = int(circleCoordinates[0].split(' ')[0])
circleY = int(circleCoordinates[0].split(' ')[1])

R = int(circleCoordinates[1])

with open('dots.txt', 'r') as f:
    dots = f.read().splitlines()

for i in dots:
    dotX = int(i.split(' ')[0])
    dotY = int(i.split(' ')[1])
    if Formula(dotX, dotY, circleX, circleY) < R:
        print(1)
    elif Formula(dotX, dotY, circleX, circleY) > R:
        print(2)
    else:
        print(0)
