ogStr = input("Enter the string: ")
n = int(input("Enter the number of positions: "))

print(ogStr[n : ] + ogStr[: n])