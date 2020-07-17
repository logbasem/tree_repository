"""In this code I will try to make an example format for how I would print a tree."""

def space(num):
    return(" " * num)

def branch(num):
    return((space(4) + "\\") * num)
"""
print(1)
print("|" + space(4) + "\\")
print("2" + space(5) + "3")
print("|" + space(2) + "\\" + space(2) + "|" + space(2) + "\\")
print("4" + space(3) + "5" + space(1) + "6" + space(3) + "7")
"""

value_list = []

empty_string = ""

top = input("What value do you want at the top of the tree? ")

branch_amount = int(input("How many branches do you want off of that? "))

for i in range(branch_amount):
        branch_value = input("Enter a branch value: ")
        value_list.append(branch_value)

for i in range(branch_amount):
    empty_string = empty_string + value_list[i] + space(4)

print(top)

if branch_amount == 1:
    print("|")
elif branch_amount > 1:
    print("|" + branch(branch_amount - 1))

print(empty_string)