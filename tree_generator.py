def space(num):
    return(" " * num)

def branch(amount, spacing=4):
    return("|" + ((space(spacing) + "\\") * (amount-1)))
    

empty_string = ""

top = 1

branch_amount = 3

value_list = [2,3,4]

for i in range(branch_amount):
    empty_string = empty_string + str(value_list[i]) + space(4)

print(top)

if branch_amount == 1:
    print("|")
elif branch_amount > 1:
    print(branch(branch_amount))

print(empty_string)