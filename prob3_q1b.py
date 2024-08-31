InputStr = input("Enter a string: ")

InputChr = input("Enter a character: ")

Str_new = InputStr.lower()
Chr_new = InputChr.lower()
revStr = InputStr[: : -1]

for i in range(len(InputStr)):
    if InputStr[i] == InputChr:
        print(f"First index = {i}")
        
    if revStr[i] == InputChr:
        print(f"last index = {len(revStr) - i -1}")
        break