ASCII_SIZE = 256
str = input("Enter a string")

def getMaxOccuringChar(str):

    count = [0] * ASCII_SIZE


    max = -1
    c = ''


    for i in str:
        count[ord(i)] += 1

    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i

    return c
p_count=getMaxOccuringChar(str)
print(p_count)