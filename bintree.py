class node:
    def __init__(self, keyval):
        self.right = self.left = None
        self.parent = None
        self.key = keyval

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

def search(tree, key):
    if tree == None or tree.key == key:
        return tree
    if tree.key <= key:
        return search(tree.right, key)
    else:
        return search(tree.left, key)

def max(tree):
    if tree.right == None:
       return tree.key 
    else:
        return max(tree.right)     

def min(tree):
    if tree.left == None:
       return tree.key 
    else:
        return min(tree.left)

def printtree(tree):
    if tree is not None:
        printtree(tree.left)
        print(tree.key)
        printtree(tree.right)


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
                print("hallo")
                return tree
            else:
                tree = tree.left
        return tree.right


def predecessor(tree, node):
    prev = None
    if min(tree) == node.key:
        return None
    while(tree.key != node.key):
        if tree.key < node.key:
            prev = tree
            tree = tree.right
        else:
            prev = tree
            tree = tree.left
    if tree.left is None:
        while(tree.parent.key > node.key):
            tree = tree.parent
        return tree.parent.key
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
    #print(search(T,30).key)
    #print(max(T))
    #print(min(T))
    #print(successor(T,N).key)
    #print("test")
    print(predecessor(T,node(55)))
  
if __name__ == "__main__":
    main()




