import tkinter as tk
from tkinter import scrolledtext
import heapq

# ---------------- AVL TREE ----------------

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:

    def get_height(self, node):
        if node:
            return node.height
        return 0

    def get_balance(self, node):
        if node:
            return self.get_height(node.left) - self.get_height(node.right)
        return 0

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):

        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def preorder(self, root):

        if root:
            output.insert(tk.END, str(root.key) + " ")
            self.preorder(root.left)
            self.preorder(root.right)


# ---------------- GUI FUNCTIONS ----------------

def avl_demo():

    output.delete(1.0, tk.END)

    avl = AVLTree()

    root = None

    data = [20, 4, 15, 70, 50, 100, 80]

    for i in data:
        root = avl.insert(root, i)

    output.insert(tk.END, "AVL Tree Preorder:\n")
    avl.preorder(root)


def heap_demo():

    output.delete(1.0, tk.END)

    data = [9, 5, 6, 2, 3]

    minheap = data.copy()
    heapq.heapify(minheap)

    maxheap = [-x for x in data]
    heapq.heapify(maxheap)

    output.insert(tk.END, "Min Heap:\n")
    output.insert(tk.END, str(minheap))

    output.insert(tk.END, "\n\nMax Heap:\n")
    output.insert(tk.END, str([-x for x in maxheap]))


def priority_demo():

    output.delete(1.0, tk.END)

    pq = []

    heapq.heappush(pq, (2, "Backup Database"))
    heapq.heappush(pq, (1, "Emergency Patient"))
    heapq.heappush(pq, (3, "Run Diagnostics"))

    output.insert(tk.END, "Priority Queue:\n\n")

    while pq:
        p, task = heapq.heappop(pq)
        output.insert(tk.END, f"Priority {p} --> {task}\n")


# ---------------- GUI ----------------

root = tk.Tk()

root.title("AVL Tree, Heap and Priority Queue")

root.geometry("700x500")

title = tk.Label(root,
                 text="AVL Tree | Heap | Priority Queue",
                 font=("Arial",18,"bold"))

title.pack(pady=10)

btn1 = tk.Button(root,
                 text="AVL Tree",
                 width=20,
                 bg="green",
                 fg="white",
                 command=avl_demo)

btn1.pack(pady=5)

btn2 = tk.Button(root,
                 text="Heap",
                 width=20,
                 bg="blue",
                 fg="white",
                 command=heap_demo)

btn2.pack(pady=5)

btn3 = tk.Button(root,
                 text="Priority Queue",
                 width=20,
                 bg="orange",
                 command=priority_demo)

btn3.pack(pady=5)

output = scrolledtext.ScrolledText(root,
                                   width=80,
                                   height=18)

output.pack(pady=15)

root.mainloop()
