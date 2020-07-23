def space(num):
    return(" " * num)

def branch(amount, spacing=4):
    return("|" + ((space(spacing) + "\\") * (amount-1)))

def add_branches(branch_amount, spacing=4):
    if branch_amount == 1:
        print("|")
    elif branch_amount > 1:
        print(branch(branch_amount,spacing))

def add_values(value_list, spacing=4):
    placeholder_string = ""
    for i in range(len(value_list)):
        placeholder_string += str(value_list[i]) + space(spacing)
    print(placeholder_string)

top = 1

spacing = 5

print(top)

add_branches(3,spacing)

add_values([2,3,4],spacing)

add_branches(2,spacing-2)

add_values([5,6],spacing-2)