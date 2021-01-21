student={"id":1,"name":"ajin","total":450}
if("name" in student):
    print(student["name"])


if("course" in student):
    print("exit")
else:
    student["course"]="btech"
print(student["course"])


if(student["total"]<500):
    student["total"]+=150
print(student["total"])

student["id"]=2
print(student["id"])
print(student)