lst=["tcs","ey","wipro","fff"]
c_name=input("Enter compNY Name")
flag=0
for comp in lst:
    if(c_name==comp):
        flag+=1

if(flag==0):
    print("not Found")
else:
    print("found")
