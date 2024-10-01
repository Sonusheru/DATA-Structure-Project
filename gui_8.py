import tkinter as tk
from anytree import Node as AnyNode, RenderTree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_larger_node = self._get_min(root.right)
            root.val = min_larger_node.val
            root.right = self._delete(root.right, min_larger_node.val)
        return root

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        res = []
        if root:
            res = self._inorder_traversal(root.left)
            res.append(root.val)
            res = res + self._inorder_traversal(root.right)
        return res

    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self._preorder_traversal(root.left)
            res = res + self._preorder_traversal(root.right)
        return res

    def postorder_traversal(self):
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, root):
        res = []
        if root:
            res = self._postorder_traversal(root.left)
            res = res + self._postorder_traversal(root.right)
            res.append(root.val)
        return res

    def display_tree(self):
        if self.root is not None:
            anytree_root = self._create_anytree_node(self.root)
            tree_structure = ""
            for pre, _, node in RenderTree(anytree_root):
                tree_structure += f"{pre}{node.name}\n"
            return tree_structure
        return "Tree is empty."

    def _create_anytree_node(self, node):
        anytree_node = AnyNode(str(node.val))
        if node.left:
            anytree_node.children = (*anytree_node.children, self._create_anytree_node(node.left))
        if node.right:
            anytree_node.children = (*anytree_node.children, self._create_anytree_node(node.right))
        return anytree_node

class BinaryTreeApp:
    def __init__(self, root):
        self.root = root
        self.bt = BinaryTree()
        self.root.title("Binary Tree Operations - Shreeraj S075")

        self.label = tk.Label(root, text="Enter a value:")
        self.label.grid(row=0, column=0)

        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=1)

        self.insert_btn = tk.Button(root, text="Insert", width=12, command=self.insert_value)
        self.insert_btn.grid(row=1, column=0)

        self.delete_btn = tk.Button(root, text="Delete", width=12, command=self.delete_value)
        self.delete_btn.grid(row=1, column=1)

        self.inorder_btn = tk.Button(root, text="Inorder Traversal", width=12, command=self.show_inorder)
        self.inorder_btn.grid(row=2, column=0)

        self.preorder_btn = tk.Button(root, text="Preorder Traversal", width=12, command=self.show_preorder)
        self.preorder_btn.grid(row=2, column=1)

        self.postorder_btn = tk.Button(root, text="Postorder Traversal", width=12, command=self.show_postorder)
        self.postorder_btn.grid(row=3, column=0)

        self.display_btn = tk.Button(root, text="Display Tree", width=12, command=self.display_tree)
        self.display_btn.grid(row=3, column=1)

        self.output_text = tk.Text(root, height=15, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2)

    def insert_value(self):
        try:
            value = int(self.entry.get())
            self.bt.insert(value)
            self.output_text.insert(tk.END, f"Inserted {value} into the tree.\n")
        except ValueError:
            self.output_text.insert(tk.END, "Error: Please enter a valid integer.\n")

    def delete_value(self):
        try:
            value = int(self.entry.get())
            self.bt.delete(value)
            self.output_text.insert(tk.END, f"Deleted {value} from the tree.\n")
        except ValueError:
            self.output_text.insert(tk.END, "Error: Please enter a valid integer.\n")

    def show_inorder(self):
        traversal = self.bt.inorder_traversal()
        self.output_text.insert(tk.END, f"Inorder Traversal: {traversal}\n")

    def show_preorder(self):
        traversal = self.bt.preorder_traversal()
        self.output_text.insert(tk.END, f"Preorder Traversal: {traversal}\n")

    def show_postorder(self):
        traversal = self.bt.postorder_traversal()
        self.output_text.insert(tk.END, f"Postorder Traversal: {traversal}\n")

    def display_tree(self):
        tree_structure = self.bt.display_tree()
        self.output_text.insert(tk.END, f"Tree Structure:\n{tree_structure}\n")

def main():
    root = tk.Tk()
    app = BinaryTreeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()