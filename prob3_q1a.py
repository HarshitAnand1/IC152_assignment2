InputStr = input("Enter a string: ")

InputChr = input("Enter a character: ")

Str_new = InputStr.lower()
Chr_new = InputChr.lower()

ind_first = Str_new.find(Chr_new)
ind_last = Str_new.rfind(Chr_new)

print(f"first index = {ind_first}")
print(f"last index = {ind_last}")