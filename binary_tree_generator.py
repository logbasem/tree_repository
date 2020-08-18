import treelib

from treelib import Node, Tree

import random

def add_two_branches(tree,parent,first_value,second_value,id_value):
    tree.create_node(str(first_value),id_value,parent=parent)
    tree.create_node(str(second_value),id_value+1,parent=parent)

def create_tree(value_list):
    binary_tree = Tree()
    binary_tree.create_node(str(value_list[0]),0)

    a = 1
    b = 2
    id_value = 1

    for i in range((len(value_list)-1)/2):
        
        add_two_branches(binary_tree,i,value_list[i+a],value_list[i+b],id_value)
        id_value += 2

        a += 1
        b = a+1

    return(binary_tree)

def list_of_numbers(min, max):
    number_list = []
    for i in range(random.randint(3,33)):
        number_list.append(random.randint(min,max))
    return number_list

value_list = list_of_numbers(1,100)
my_tree = create_tree(value_list)
my_tree.show()

for i in range(len(value_list)-1):
    print(my_tree[i].tag)