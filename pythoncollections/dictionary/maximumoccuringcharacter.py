pattern="ABABBACEEEEEE"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
for key,value in dict.items():
    print(key,"",value)

print(dict.get("E"))
#get --.to get the value of corresponding key


result=sorted(dict,key=dict.get,reverse=True)
print(result[0])