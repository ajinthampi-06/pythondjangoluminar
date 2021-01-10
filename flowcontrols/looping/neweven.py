limit=int(input("Enter the limit"))
lower=int(input("Enter the lower limit"))

while lower<=limit:
    if(lower%2==0):
        print(lower)
    lower+=1

