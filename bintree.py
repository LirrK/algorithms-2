class node:
    def __init__(self, keyval):
        self.right = self. left = None
        self.key = keyval

def insert(tree, newnode):
    if tree is None:
        tree = newnode
    else:
        if tree.key <= newnode.key:
            if tree.right is None:
                tree.right = newnode
            else:
                insert(tree.right, newnode)
        else:
            if tree.left is None:
                    tree.left = newnode
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

    
 
def main():
    T = node(50)
    N = node(20)
    insert(T,node(30)) 
    insert(T,node(20)) 
    insert(T,node(40)) 
    insert(T,node(70)) 
    insert(T,node(60)) 
    insert(T,node(80))
    #printtree(T)
    #print(search(T,30).key)
    #print(max(T))
    #print(min(T))
    print(successor(T,N).key)
  
if __name__ == "__main__":
    main()




