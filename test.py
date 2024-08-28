from collections import deque
import json


class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
        # self.left = None
        # self.right = None


"""
Root node
//add to the list

        // check child nodes
        // point to root node
// [Root, child1, child2, child11, child12 child 21, child22]

"""


def flatting_tree(root):
    #base case
    if root is None:
        return []

    queue = deque([root])
    flat_list = []
    while queue:
        node = queue.popleft()
        flat_list.append(node.name)
        for child in node.children:
            queue.append(child)
    return flat_list


# root = Node(1)
#
# child1 = Node(2)
# child2 = Node(3)
#
# root.children = [child1, child2]
# child11 = Node(4)
# child12 = Node(5)
#
# child1.children = [child11, child12]
#
# child21 = Node(6)
# child22 = Node(7)
#
# child2.children = [child21, child22]

def create_tree(tree):
    if not tree:
        return

    for node_name, data in tree.items():
        current_node = Node(node_name, data.get("value"))
        children = data.get("children", [])
        for child in children:
            current_node.children.append(create_tree(child))
    return current_node


if __name__ == '__main__':
    with open("tree_struct.json", "r") as file:
        tree_struct = json.load(file)

    # print(tree_struct)
    root = create_tree(tree_struct)
    print(flatting_tree(root))
