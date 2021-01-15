##empty list
#lst=[]
lst=list()#creating an empty list




## method for adding element to list
#lst.append(50)
#lst.append(60)
#print(lst)

#print 10 to 50
for i in range(1,51):
    lst.append(i)
print(lst)
total=sum(lst)
print(total)


##highest elemet
high=max(lst)
print(high)


#$min
mini=min(lst)
print(mini)