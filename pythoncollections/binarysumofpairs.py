lst=[1,2,3,4,5]
element=int(input("enter element"))
low=0
upp=len(lst)-1
pair_list=[]
while(low<upp):
    tot=lst[low]+lst[upp]
    if (element==tot):
        pair_list.append((lst[low],lst[upp]))

    elif(element<tot):
        upp-=1

    elif(element>tot):
        low+=1
#print(pair_list)


