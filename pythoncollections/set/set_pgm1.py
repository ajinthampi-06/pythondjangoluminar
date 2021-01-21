#define  ===
#st={}#//empty{} takem as dictionary
#use set() function to create empty set


#st=set()
st={10,11,12,13,"hello",15,156}
print(type(st))
print(st)

#insertion order is not preserved
#indexing is not posiible
st2={50,60}
st.update(st2)##updation possible
#duplicates are not allowed