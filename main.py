import time
iport random
oints = 0
l1 = [0, 1]
nq = 0
woans = 0
qcount = 1te.sleep(2)
gamestartend = input("\npress enter to start\n")
ii = time.time()
wile 1:
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
pint("--------------\nTIME'S UP!!!\n--------------")
print()
pint(f"YOU SCORED {points} POINTS-\nATTEMPTED {noq + wroans} QUESTIONS,\n\nANSWERED {noq} QUESTIONS CORRECTLY   ,AND\n         {wroans} QUESTIONS INCORRECTLY")
gmestartend = input("\npress enter to exit")
