def space(num):
    return(" " * num)

def branch(amount, spacing=4):
    return("|" + ((space(spacing) + "\\") * (amount-1)))

def add_branches(branch_amount, spacing=4):
    if branch_amount == 1:
        return("|")
    elif branch_amount > 1:
        return(branch(branch_amount,spacing))

def add_values(value_list, spacing=4):
    placeholder_string = ""
    for i in range(len(value_list)):
        placeholder_string += str(value_list[i])
        if i != (len(value_list)-1):
            placeholder_string+= space(spacing)
    return(placeholder_string)

top = 1

spacing = 4

tiers = []

tiers.append(top)

tiers.append(add_branches(2,spacing))

tiers.append(add_values([2,3],spacing))

tiers.append(add_branches(1,spacing-2) + space(spacing) + add_branches(2,spacing-2,))

tiers.append(add_values([4],spacing-2) + space(spacing) + add_values([5,6],spacing-2))

for tier in tiers:
    print(tier)