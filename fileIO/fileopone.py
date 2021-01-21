#read
#step1  :we have to create a refernce
#f=opem("filepath","mode")
word=[]
f=open("demo","r")
#for lines in f:
  #  print(lines)



for lines in f:
    word.append(lines.rstrip("\n").split(" "))
print(word)
mywords=[]
for wrd in word:
    for mywrd in wrd:
        mywords.append(mywrd)
print(mywords)