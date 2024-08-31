# Taking two strings of same length as input
str1 = input("Enter a string: ")
str2 = input("Enter another string of same length: ")

AnsStr=""
for i in range (0,len(str1),2):
    
    if str1[i] == str2[i]:
        AnsStr = AnsStr + str1[i]

print(AnsStr)
