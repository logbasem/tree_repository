def space(num):
    return(" " * num)

def branch(num):
    return((space(4) + "\\") * num)
    
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