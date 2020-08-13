import treelib

from treelib import Node, Tree


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

    binary_tree.show()

value_list = [4,2,2]

create_tree(value_list)