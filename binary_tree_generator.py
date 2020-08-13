import treelib

from treelib import Node, Tree



def add_two_branches(tree,parent,first_value,second_value):
    tree.create_node(str(first_value),first_value,parent=parent)
    tree.create_node(str(second_value),second_value,parent=parent)

def create_tree(value_list):
    binary_tree = Tree()
    binary_tree.create_node(str(value_list[0]),value_list[0])

    a = 1
    b = 2

    for i in range((len(value_list)-1)/2):
        
        add_two_branches(binary_tree,value_list[i],value_list[i+a],value_list[i+b])
        
        a += 1
        b = a+1

    binary_tree.show()

value_list = [330,33,10,11,3,5,2]

create_tree(value_list)