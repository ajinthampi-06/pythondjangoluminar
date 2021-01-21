lst=[10,8,7,11,12,6,5]

#step1 sort the list
# lower and upper
#calculate mid  low+upp//2
# if element>list(mid) true low=mid+1
#calcualte mid=low+upp//2
#element>list[mid] ture low=mid+1


#elment==list[mid]==found


lst.sort()
low=0
flag=0
upp=len(lst)-1
element=int(input("Enter element to search"))
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if(flag==0):
    print("not found")
else:
    print("element found")