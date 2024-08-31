ogStr ="In a Democracy, the government is of the people, by the people, and for the people, still people don't go out and vote"

index1 = ogStr.find("people")

newStr1 = ogStr[:index1] + "PEOPLE" + ogStr[index1+len("people"):]
print(newStr1)

index2 = newStr1.find("people")
newStr2 = newStr1[:index2] + "pEOPLE" + newStr1[index2+len("people"):]
print(newStr2)

index3 = newStr2.find("people")
newStr3 = newStr2[:index3] + "pEOPLE" + newStr2[index3+len("people"):]
print(newStr3)

index4 = newStr3.find("people")
newStr4 = newStr3[:index4] + "peoPLE" + newStr3[index4+len("people"):]
print(newStr4)
