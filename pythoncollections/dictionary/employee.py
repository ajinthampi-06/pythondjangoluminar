employee={"id":100,"enmae":"ajay","exp":2,"salary":35000}
if("salary" in employee):
    print(employee["salary"])



##to check gender key
if("gender" in employee):
    print("exit")
else:
    employee["gender"]="male"
print(employee)

#if employee salary<35000 add 5000 more
if(employee["salary"]<=35000):
    employee["salary"]+=5000
print(employee)

