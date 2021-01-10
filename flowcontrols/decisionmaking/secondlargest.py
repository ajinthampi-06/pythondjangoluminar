num1=int(input("enter  number1"))
num2=int(input("enter  number2"))
num3=int(input("enter  number3"))


if(num1>num2)&(num1>num3):
    print("num1 is largest")
    large=num1
    if(num2>num3):
        print("num 2 is second largest")
        second=num2
        third=num3
    else:
        print("num 3 is second largest")
        second=num3
        third=num2

elif(num2>num1)&(num2>num3):
    print("num 2 is large")
    large=num2
    if(num3>num1):
        print("num 3 is second largest")
        second=num3
        third=num1
    else:
        print("num 1 is second largest")
        second=num1
        third=num3
elif(num3>num1)&(num3>num2):
    print("num 3 is large")
    large=num3
    if(num1>num2):
        print("num1 is second largest")
        second=num1
        third=num2
    else:
        print("num 2 is second largest")
        second=num2
        third=num1
elif(num1==num3)&(num1==num2):
    print("3 numbers are same")


print("sorted numbers are",large,"",second,"",third)




