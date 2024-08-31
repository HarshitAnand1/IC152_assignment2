ogStr ="In a Democracy, the government is of the people, by the people, and for the people, still people don't go out and vote"

newStr1 = ogStr.replace("people", "PEOPLE",1)
print(newStr1)

newStr2 = newStr1.replace("people", "pEOPLE", 2)
print(newStr2)

newStr3 = newStr2.replace("people", "peoPLE")
print(newStr3)