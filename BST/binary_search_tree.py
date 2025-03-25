class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def update(self, root, old_key, new_key):
        root = self.delete(root, old_key)
        return self.insert(root, new_key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        return root

    def minValueNode(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")

    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self.search(root.left, key)
        return self.search(root.right, key)
