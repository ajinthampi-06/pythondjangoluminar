num1=int(input("enter  number1"))
num2=int(input("enter  number2"))
num3=int(input("enter  number3"))

#find 2nd largest
#sort the 3 nos
if(num1>num2)&(num1>num3):
    print("num1 is largest")
elif(num2>num1)&(num2>num3):
    print("num 2 is large")
elif(num3>num1)&(num3>num2):
    print("num 3 is large")
elif(num1==num3)&(num1==num2):
    print("3 numbers are same")