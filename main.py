import time
import random

points = 0
l1 = [0, 1]
noq = 0
wroans = 0
qcount = 1

print("WELCOME TO MY GAME\nINSTRUCTIONS:-\nYOU HAVE TO SOLVE AS MANY MATH PROBLEMS AS YOU CAN IN 1 MINUTE TIME\n"
      "EACH CORRECT ANSWER GIVES YOU 20 POINTS BUT EACH INCORRECT ANSWER DEDUCTS 5 POINTS\n")
time.sleep(2)
gamestartend = input("\npress enter to start\n")
ini = time.time()
while 1:
    fin = time.time()
    if fin - ini >= 60:
        break

    opctrl = random.choice(l1)
    if opctrl == 1:
        oppr = "+"
        op = (lambda a, b: a+b)
    elif opctrl == 0:
        oppr = "-"
        op = (lambda a, b: a-b)

    no1 = random.randrange(10, 50)
    no2 = random.randrange(60, 100)

    print("------------\nQUESTION", qcount, "\n------------\n")
    qcount += 1
    print(f"What is {no2} {oppr} {no1}")
    # noinspection PyUnboundLocalVariable
    corans = op(no2, no1)
    userinp = int(input("enter your answer -\n"))

    if userinp == corans:
        print("\nCorrect, +20 Points!!\n")
        noq += 1
        points += 20
    else:
        print("\nIncorrect, -5 Points\n")
        points -= 5
        wroans += 1
print("--------------\nTIME'S UP!!!\n--------------")
print()
print(f"YOU SCORED {points} POINTS-\nATTEMPTED {noq + wroans} QUESTIONS,\n\nANSWERED {noq} QUESTIONS CORRECTLY   ,AND\n         {wroans} QUESTIONS INCORRECTLY")
gamestartend = input("\npress enter to exit")
