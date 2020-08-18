"""
This code prints a tree using key functions and variables that can be entered.
"""

#a function that creates a space given a multiplier value
def space(num):
    return(" " * num)

#returns a string of branches based on a given branch amount and spacing value
def branch(amount, spacing=4):
    return("|" + ((space(spacing) + "\\") * (amount-1)))

#does the same as the above function, but can also print a single branch
def add_branches(branch_amount, spacing=4):
    if branch_amount == 1:
        return("|")
    elif branch_amount > 1:
        return(branch(branch_amount,spacing))

#returns a string of values given a list of values and a spacing value
def add_values(value_list, spacing=4):
    placeholder_string = ""
    for i in range(len(value_list)):
        placeholder_string += str(value_list[i])
        if i != (len(value_list)-1):
            placeholder_string+= space(spacing)
    return(placeholder_string)

#the value at the top of the tree
top = 1

#the amount of tiers in the tree
tier_amount = 3

#how spaced out the tree needs to be, relative to the amount of tiers it has
spacing = tier_amount*2

#declares an empty list of tiers
tiers = []

#adds top tear
tiers.append(top)

#adds second tier
tiers.append(add_branches(3,spacing))
tiers.append(add_values([2,3,4],spacing))

#adds third tier
tiers.append(add_branches(1,int(spacing/2)) + space(spacing) + add_branches(2,int(spacing/2)))
tiers.append(add_values([5],int(spacing/2)) + space(spacing) + add_values([6,7],int(spacing/2)))

#prints each tier
for tier in tiers:
    print(tier)