import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid Position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid Position")
        return self.items.pop(position)

    def peek(self):
        if not self.items:
            raise IndexError("Stack is Empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            return "Stack is Empty"
        return " <- ".join(reversed(self.items))


stack = Stack()


def insert_item():
    item = entry_item.get()
    pos = entry_pos.get()

    if item == "" or pos == "":
        messagebox.showerror("Error", "Enter Item and Position")
        return

    try:
        stack.insert(item, int(pos))
        update_stack()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_item():
    pos = entry_pos.get()

    if pos == "":
        messagebox.showerror("Error", "Enter Position")
        return

    try:
        item = stack.delete(int(pos))
        messagebox.showinfo("Deleted", f"{item} Deleted")
        update_stack()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def peek_item():
    try:
        messagebox.showinfo("Top Item", stack.peek())
    except Exception as e:
        messagebox.showerror("Error", str(e))


def traverse():
    messagebox.showinfo("Stack", stack.traverse())


def size():
    messagebox.showinfo("Size", str(stack.size()))


def empty():
    if stack.is_empty():
        messagebox.showinfo("Status", "Stack is Empty")
    else:
        messagebox.showinfo("Status", "Stack is Not Empty")


def update_stack():
    label_stack.config(text=stack.traverse())
    entry_item.delete(0, tk.END)
    entry_pos.delete(0, tk.END)


root = tk.Tk()
root.title("Stack GUI")
root.geometry("450x420")
root.resizable(False, False)

tk.Label(root, text="Stack Operations", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Item").pack()
entry_item = tk.Entry(root, width=25)
entry_item.pack()

tk.Label(root, text="Position (0-Based Index)").pack()
entry_pos = tk.Entry(root, width=25)
entry_pos.pack(pady=5)

tk.Button(root, text="Insert", width=18, command=insert_item).pack(pady=3)
tk.Button(root, text="Delete", width=18, command=delete_item).pack(pady=3)
tk.Button(root, text="Peek", width=18, command=peek_item).pack(pady=3)
tk.Button(root, text="Traverse", width=18, command=traverse).pack(pady=3)
tk.Button(root, text="Size", width=18, command=size).pack(pady=3)
tk.Button(root, text="Is Empty", width=18, command=empty).pack(pady=3)

tk.Label(root, text="Current Stack", font=("Arial", 12, "bold")).pack(pady=10)

label_stack = tk.Label(
    root,
    text="Stack is Empty",
    bg="white",
    relief="sunken",
    width=40,
    height=2
)
label_stack.pack()

root.mainloop()
