#values stored in dictionary form of key value pair
#fetch valuess using key
#key must be unique

expenses={"jan":3000,"feb":400000,"mar20":28000}
print(expenses["feb"])
print("june20" in expenses)##check availibility of key
# adding new key value pairs
expenses["june20"]=25000
print(expenses)
print("mar20" in expenses)
expenses["mar20"]-=3000
print(expenses["mar20"])

