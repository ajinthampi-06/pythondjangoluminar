pattern="ABABBAC"
for ch in pattern:
    if ch not in pattern:
        dict[ch]=1
    else:
        print(ch,"first recursive character")
        break
