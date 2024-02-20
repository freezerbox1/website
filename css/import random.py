import random

P=0
Z=0
Y=0


def flip():
    X = random.randint(1,2)
    if X == 1:
        Y +=1
    if X == 2:
        Z += 1


while P >= 100:
    flip
    P += 1

print(Y)
print(Z)
