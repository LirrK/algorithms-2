# ***The only class: node***
# ° We decided to only use a node class and create
#   an object called 'tree' or 'T' which is the root
#   and somewhat the entry to the data structure.
# ° Every object contains pointer to its left and right
#   child node, aswell as to its parent node.
# ° Every object contains a value 'key'.
class node:
    def __init__(self, keyval):
        self.right = self.left = None
        self.parent = None
        self.key = keyval

# ***Adds a node to a tree (recursive)***
# ° at 'binary search tree'-sorted position
# ° If there is no tree now, newnode becomes root
#   of the tree.
def insert(tree, newnode):
    if tree is None:
        tree = newnode
    else:
        if tree.key <= newnode.key:
            if tree.right is None:
                tree.right = newnode
                tree.right.parent = tree
            else:
                insert(tree.right, newnode)
        else:
            if tree.left is None:
                tree.left = newnode
                tree.left.parent = tree
            else:
                insert(tree.left, newnode)

# ***Returns pointer to node with value 'key' (recursive)***
# ° returns None if there is no tree
def search(tree, key):
    if tree == None or tree.key == key:
        return tree
    if tree.key <= key:
        return search(tree.right, key)
    else:
        return search(tree.left, key)

# ***Returns pointer to node with MAXIMUM value in tree (recursive)***
# ° The maximum value in a BST is found in the
#   leaf of the most right path.
def max(tree):
    if tree.right == None:
       return tree.key 
    else:
        return max(tree.right)     

# ***Returns pointer to node with MINIMUM value in tree (recursive)***
# ° The minimum value in a BST is found in the
#   leaf of the most left path.
def min(tree):
    if tree.left == None:
       return tree.key 
    else:
        return min(tree.left)

# ***Prints every value on the output stream (recursive)***
# ° One value per line.
# ° From lowest to highest value.
def printtree(tree):
    if tree is not None:
        printtree(tree.left)
        print(tree.key)
        printtree(tree.right)

# ***Returns node with minimum bigger key value than 'node'***
def successor(tree, node):
    if node.right != None:
        return min(node.right)
    else:
        while(tree.key != node.key):
            if min(tree) != node.key and max(tree) != node.key:
                if tree.key < node.key:
                    tree = tree.right
                else:
                    tree = tree.left
            elif min(tree) == node.key and tree.left.key == node.key:
                return tree
            else:
                tree = tree.left
        return tree.right

# ***Return node with maximum smaller key value than 'node'***
def predecessor(tree, node):
    # Since the minimum value has no predecessor -> return None
    if min(tree) == node.key:
        return None
    # Finding node in tree with same value as 'node'.
    # When while-loop stops, 'tree' is the node with the value
    # we searched for.
    while(tree.key != node.key):
        if tree.key < node.key:
            tree = tree.right
        else:
            tree = tree.left
    # If tree.left is None then the maximum smaller key value
    # has to be in another branch.
    # This part uses the pointer on the parent node to go back
    # on the branch till there is a value smaller than node's value.
    # Then it returns that node with the value smaller than nodes's.
    if tree.left is None:
        while(tree.parent.key > node.key):
            tree = tree.parent
        return tree.parent.key
    # If tree.left exists, it must be smaller than node's key value
    # and it also has to be the biggest value in this subtree.
    # Using max() to find the biggest value in subtree.
    else:
        return max(tree.left)

 
def main():
    T = node(50)
    N = node(20)
    N2 = node(70)
    N3 = node(80)
    insert(T,node(30)) 
    insert(T,node(20)) 
    insert(T,node(40)) 
    insert(T,node(70)) 
    insert(T,node(60)) 
    insert(T,node(80))
    insert(T,node(15))
    insert(T,node(25))
    insert(T,node(35))
    insert(T,node(45))
    insert(T,node(55))
    insert(T,node(65))
    insert(T,node(75))
    insert(T,node(85))
    insert(T,node(85))
    insert(T,node(60))
    #printtree(T)
    print(search(T,40).key)
    print(max(T))
    print(min(T))
    print(successor(T,N).key)
    print(predecessor(T,node(55)))
  
if __name__ == "__main__":
    main()




