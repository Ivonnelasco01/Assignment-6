print("Addition Quiz")
score = 0

q1 = int(input("1 + 2 = "))#3
if q1 == 3 or q1 != 3:
    if q1 == 3:
        print("Correct")
        score+=1
    else:
        print("Incorrect")

q2 = int(input("3 + 4 = ")) #7
if q2 == 7 or q2 != 7:
    if q2 == 7:
        print("Correct")
        score+= 1
    else:
        print("Incorrect")

q3 = int(input("5 + 6 = ")) #11
if q3 == 11 or q3 != 11:
    if q3 == 11:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

q4 = int(input("7 + 8 = ")) #15
if q4 == 15 or q4 != 15:
    if q4 == 15:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

q5 = int(input("10 + 11 = ")) #21
if q5 == 21 or q5 != 21:
    if q5 == 7:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

q6 = int(input("12 + 13 = ")) #25
if q6 == 25 or q2 != 25:
    if q6 == 25:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

q7 = int(input("14 + 15 = ")) #29
if q7 == 29 or q7 != 29:
    if q7 == 29:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

q8 = int(input("16 + 17 = ")) #33
if q8 == 33 or q8 != 33:
    if q8 == 7:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

q9 = int(input("18 + 19 = ")) #37
if q9 == 37 or q9 != 37:
    if q9 == 37:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

q10 = int(input("20 + 21 = ")) #41
if q10 == 41 or q2 != 41:
    if q10 == 41:
            print("Correct")
            score += 1
    else:
        print("Incorrect")

print("Result: ", score,"/ 10")