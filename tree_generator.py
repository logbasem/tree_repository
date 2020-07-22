def space(num):
    return(" " * num)

def branch(amount, spacing=4):
    return("|" + ((space(spacing) + "\\") * (amount-1)))

def add_values(value_list, spacing=4):
    placeholder_string = ""
    for i in range(branch_amount):
        placeholder_string += str(value_list[i]) + space(spacing)
    return placeholder_string

top = 1

branch_amount = 3

value_list = [2,3,4]

print(top)

if branch_amount == 1:
    print("|")
elif branch_amount > 1:
    print(branch(branch_amount))

print(add_values(value_list))