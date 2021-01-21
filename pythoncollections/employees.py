employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000],

]


##print number of employees in this company
number_of_employees=len(employees)
print("no of employess",number_of_employees)


## print how much salary conpany has to rais in month end


total_amount=0
for emp in employees:
    total_amount+=emp[3]
print("total_amount",total_amount)



##group by designation
d_cnt,da_cnt,ba_cnt=0,0,0
for emp in employees:
    if emp[2]=="dataanalyst":
        da_cnt+=1
    elif emp[2]=="developer":
        d_cnt+=1
    else:
        ba_cnt+=1
print("data analyst=",da_cnt,"developer=",d_cnt," ba count=",ba_cnt)





### print highest salaried employee

salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
high_salary=max(salary_list)
print("highest salary =",high_salary)

for emp in employees:
    if emp[3]==high_salary:
        print(emp)




##print employeeb name who recive lowest salary whosw designatyion==developer
d_sallist=[]
for emp in employees:
    if emp[2]=="developer":
        d_sallist.append(emp[3])
low_sal=min(d_sallist)
for emp in employees:
    if(emp[2]=="developer")&(emp[3]==low_sal):
        print("lowest salary=",emp)