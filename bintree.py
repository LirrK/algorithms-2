import os

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
# ° Second if-clause prevents the function to insert
#   node with a value it already has.
def insert(tree, newnode):
    if tree is None:
        tree = newnode
    else:
        if search(tree, newnode.key) != None:
            if search(tree, newnode.key).key == newnode.key:
                return
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
    if node.key == max(tree):
        return None
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

# ***Returns node with maximum smaller key value than 'node'***
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
        return tree.parent
    # If tree.left exists, it must be smaller than node's key value
    # and it also has to be the biggest value in this subtree.
    # Using max() to find the biggest value in subtree.
    else:
        return search(tree,max(tree.left))

# ***Creates a tree.dot file***
#   in the same dir as the code
# ° .dot files can be read by GraphViz interpreters,
#   which than create a graph.
# ° The function intself contains another printToFile
#   method which iterates over the given tree. (recursive)
def printBST(tree):

    def printToFile(tree):
        if tree is not None:
            #Left side: 
            if tree.left != None:
                #opens and writes to file tree.dot the given string
                #"a" is parameter for "append"
                with open("tree.dot", "a") as file:
                    file.write(str(tree.key) + "->" + str(tree.left.key) + ";\n")
                #recursivle goes further on the left branch
                printToFile(tree.left)
            
            #Right side:
            if tree.right != None:
                with open("tree.dot", "a") as file:
                    file.write(str(tree.key) + "->" + str(tree.right.key) + ";\n")
                printToFile(tree.right)
            
            return
    
    #creates file tree.dot and writes the given String
    #"w" is the parameter for creating and writing
    with open("tree.dot", "w") as file:
        file.write("digraph T {\n\n")

    printToFile(tree)

    #this time "a", since there is already tree.dot
    #and we just want to append the last curly bracket
    with open("tree.dot", "a") as file:
        file.write("\n}")


 
def main():

    testBool = input("Do you want to create the test tree and run tests? [y/n]\n")
    if testBool == "y":
        #creating a tree for tests
        T = node(50)       #tree (root)
        N = node(15)
        insert(T,node(30)) 
        insert(T,node(40)) 
        insert(T,node(70)) 
        insert(T,node(60)) 
        insert(T,node(80))
        insert(T,node(15))
        insert(T,node(25))
        insert(T,node(35))
        insert(T,node(45))
        insert(T,node(55))
        insert(T,node(55)) #second 55
        insert(T,node(65))
        insert(T,node(75))
        insert(T,node(85))
        insert(T,node(85)) #second 85
        insert(T,node(0))  #zero case
        insert(T,node(-10))#minus case


        # Test for printtree()
        print("Test for printtree:")
        printtree(T)
        print("----------------------------------")

        # Test for search()
        print("Test for search:")
        print(search(T,40).key)
        print("----------------------------------")

        # Test for max()
        print("Test for max:")
        print(max(T))
        print("----------------------------------")

        # Test for min()
        print("Test for min:")
        print(min(T))
        print("----------------------------------")

        # Tests for successor()
        print("Tests for successor:")
        print(successor(T,N).key)           # 25
        print(successor(T,node(55)).key)    # 60
        print(successor(T,node(80)).key)    # 85
        print(successor(T,node(-10)).key)   # 0
        print(successor(T,node(85)))        # None
        print(successor(T,node(50)).key)    # 55
        print("----------------------------------")
        
        # Tests for predecessor()
        print("Tests for predecessor:")
        print(predecessor(T,node(0)).key)   # -10
        print(predecessor(T,node(15)).key)  # 0
        print(predecessor(T,node(-10)))     # None
        print(predecessor(T,node(50)).key)  # 45
        print(predecessor(T,node(55)).key)  # 50
        print("----------------------------------")
        
        #Creating tree.dot file
        printBST(T)
    
    # ***This just coordinates the interactive part of the main function***
    # ° where one can test every function with a self crated tree
    # ° not very elegant written, but it works
    if input("Do you want to start manipulating your own tree? [y/n]") == "y":
        inputTree = node(50)
        insertInput = None
        decisionBool = True
        print("Start by inserting values.\n")
        print("Insert values one by one and accept every single one by hitting ENTER.\n")
        print("If you want to stop inserting, simply write [exit] without brackets and hit ENTER.\n")
        while(insertInput != "exit"):
            insertInput = input()
            if insertInput != "exit":
                inputTemp = int(insertInput)
                insert(inputTree, node(inputTemp))

        while(decisionBool == True):
            print("Which functionality do you want to test now?")
            print("[search][max][min][printtree][successor][predecessor][printBSD][exit]")
            decision = input("Write the functions name without brackets and hit ENTER:")
            if decision == "search":
                print("Which value you want to search for?")
                print(search(inputTree, input()))
            elif decision == "max":
                print("Maximum value is:")
                print(max(inputTree))
            elif decision == "min":
                print("Minimum value is:")
                print(min(inputTree))
            elif decision == "printtree":
                print("This is the tree from lowest to highest value:")
                printtree(inputTree)
            elif decision == "successor":
                print("For which value you want to find the successor?:")
                print(successor(inputTree, node(int(input()))).key)
            elif decision == "predecessor":
                print("For which value you want to find the predecessor?:")
                print(predecessor(inputTree, node(int(input()))).key)
            elif decision == "printBSD":
                print("The tree.dot file gets created.")
                printBST(inputTree)
                print("Success! You can find it in the same folder as this code.")
            elif decision == "exit":
                decisionBool = False
    

if __name__ == "__main__":
    main()
