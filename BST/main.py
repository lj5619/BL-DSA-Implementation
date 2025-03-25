from binary_search_tree import BinarySearchTree

def main():
    bst = BinarySearchTree()

    bst.root = bst.insert(bst.root, 50)
    bst.root = bst.insert(bst.root, 30)
    bst.root = bst.insert(bst.root, 20)
    bst.root = bst.insert(bst.root, 40)
    bst.root = bst.insert(bst.root, 70)
    bst.root = bst.insert(bst.root, 60)
    bst.root = bst.insert(bst.root, 80)

    print("Post-order traversal after insertion:")
    bst.postorder(bst.root)
    print()

    bst.root = bst.update(bst.root, 20, 25)
    print("Post-order traversal after update (replace 20 with 25):")
    bst.postorder(bst.root)
    print()

    bst.root = bst.delete(bst.root, 40)
    print("Post-order traversal after deletion (delete 40):")
    bst.postorder(bst.root)
    print()

    bst.root = bst.delete(bst.root, 50)
    print("Post-order traversal after deletion (delete 50):")
    bst.postorder(bst.root)
    print()

    node = bst.search(bst.root, 80)
    if node:
        print(f"Node with value 80 found: {node.value}")
    else:
        print("Node with value 80 not found.")

if __name__ == "__main__":
    main()
