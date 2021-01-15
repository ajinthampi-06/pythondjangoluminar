lst=[10,11,12,13,14,15,16,17]
#even numbers =>even list
#odd numbers=>odd list
lst1=list()
lst2=list()
total1=0
total2=0
for num in lst:
    if num%2==0:
        lst1.append(num)

    else:
        lst2.append(num)

print(lst1)
print("even sum",sum(lst1))
print(lst2)

print("odd sum",sum(lst2))