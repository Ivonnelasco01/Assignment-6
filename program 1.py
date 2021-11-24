def number_sort():
    num1 = input("Enter 1st number here: ")
    num2 = input("Enter 2nd number here: ")
    num3 = input("Enter 3rd number here: ")
    num4 = input("Enter 4th number here: ")

    if num1 > num2 and num1 > num3 and num1 > num4:
        if num2 > num3 and num2 > num4:
            if num3 > num4:
                print(num1, num2, num3, num4)
            else:
                print(num1, num2, num4, num3)
        elif num3 > num2 and num3 > num4:
            if num2 > num4:
                print(num1, num3, num2, num4)
            else:
                print(num1, num3, num4, num2)
        else:
            if num3 > num2:
                print(num1, num4, num3, num2)
            else:
                print(num1, num4, num2, num3)
    elif num2 > num1 and num2 > num3 and num2 > num4:
        if num1 > num3 and num1 > num4:
            if num3 > num4:
                print(num2, num1, num3, num4)
            else:
                print(num2, num1, num4, num3)
        elif num3 > num1 and num3 > num4:
            if num1 > num4:
                print(num2, num3, num1, num4)
            else:
                print(num2, num3, num4, num1)
        else:
            if num3 > num1:
                print(num2, num4, num3, num1)
            else:
                print(num2, num4, num1, num3)
    elif num3 > num1 and num3 > num3 and num3 > num4:
        if num1 > num2 and num1 > num4:
            if num2 > num4:
                print(num3, num1, num2, num4)
            else:
                print(num3, num1, num4, num2)
        elif num2 > num1 and num2 > num4:
            if num1 > num4:
                print(num3, num2, num1, num4)
            else:
                print(num3, num2, num4, num1)
        else:
            if num2 > num1:
                print(num3, num4, num2, num1)
            else:
                print(num3, num4, num1, num2)
    if num4 > num1 and num4 > num2 and num4 > num3:
        if num1 > num2 and num1 > num3:
            if num2 > num3:
                print(num4, num1, num2, num3)
            else:
                print(num4, num1, num3, num2)
        elif num2 > num1 and num2 > num3:
            if num1 > num3:
                print(num4, num2, num1, num3)
            else:
                print(num4, num2, num3, num1)
        else:
            if num2 > num1:
                print(num4, num3, num2, num1)
            else:
                print(num4, num3, num1, num2)

numberSort = number_sort()