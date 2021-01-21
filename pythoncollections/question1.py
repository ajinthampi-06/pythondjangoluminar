lst=list()
limit=int(input("Enter limit"))
for i in range(0,limit):
    number=int(input("enter number"))
    lst.append(number)
print(lst)

oplist=list()
total=sum(lst)
for num in lst:

    oplist.append(total-num)
print(oplist)