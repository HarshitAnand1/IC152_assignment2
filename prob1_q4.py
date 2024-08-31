str_1 = input("Enter the string: ")
str_1_low = str_1.lower()
str_2 = str_1_low [ : : -1]

if str_2 == str_1_low:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")
