"""In this code I will try to make an example format for how I would print a tree."""
def space(num):
    return(" " * num)

print(1)
print("|" + space(4) + "\\")
print("2" + space(4) + "3")
print("|" + space(2) + "\\" + space(1) + "|" + space(2) + "\\")
print("4" + space(2) + "5" + space(1) + "6" + space(2) + "7")