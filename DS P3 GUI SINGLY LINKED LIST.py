import tkinter as tk
from tkinter import messagebox

# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List 
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Invalid Position")

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None:
                raise IndexError("Invalid Position")
            temp = temp.next

        if temp is None:
            raise IndexError("Invalid Position")

        new_node.next = temp.next
        temp.next = new_node

    def delete_by_value(self, value):

        temp = self.head

        if temp is None:
            return False

        if temp.data == value:
            self.head = temp.next
            return True

        prev = None

        while temp:
            if temp.data == value:
                prev.next = temp.next
                return True

            prev = temp
            temp = temp.next

        return False

    def delete_by_index(self, position):

        if self.head is None:
            raise IndexError("Linked List is Empty")

        if position == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None or temp.next is None:
                raise IndexError("Invalid Position")
            temp = temp.next

        temp.next = temp.next.next

    def display(self):

        temp = self.head

        if temp is None:
            return "Linked List is Empty"

        s = ""

        while temp:
            s += str(temp.data)

            if temp.next:
                s += " → "

            temp = temp.next

        return s


# Object 
ll = LinkedList()

# Functions 

def show_list():
    lbl_result.config(text=ll.display())


def insert_begin():
    try:
        data = int(entry_data.get())
        ll.insert_at_beginning(data)
        show_list()
    except:
        messagebox.showerror("Error", "Enter Valid Data")


def insert_end():
    try:
        data = int(entry_data.get())
        ll.insert_at_end(data)
        show_list()
    except:
        messagebox.showerror("Error", "Enter Valid Data")


def insert_position():
    try:
        data = int(entry_data.get())
        pos = int(entry_position.get())

        ll.insert_at_position(data, pos)

        show_list()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_value():
    try:
        value = int(entry_data.get())

        if ll.delete_by_value(value):
            show_list()
        else:
            messagebox.showinfo("Info", "Value Not Found")

    except:
        messagebox.showerror("Error", "Enter Valid Data")


def delete_index():
    try:
        pos = int(entry_position.get())

        ll.delete_by_index(pos)

        show_list()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_boxes():
    entry_data.delete(0, tk.END)
    entry_position.delete(0, tk.END)


#GUI
root = tk.Tk()
root.title("Singly Linked List")
root.geometry("500x520")
root.resizable(False, False)

title = tk.Label(root,
                 text="SINGLY LINKED LIST",
                 font=("Arial", 18, "bold"))

title.pack(pady=10)

tk.Label(root, text="Enter Data", font=("Arial", 11)).pack()

entry_data = tk.Entry(root, width=30)
entry_data.pack(pady=5)

tk.Label(root, text="Enter Position", font=("Arial", 11)).pack()

entry_position = tk.Entry(root, width=30)
entry_position.pack(pady=5)

tk.Button(root,
          text="Insert at Beginning",
          width=25,
          command=insert_begin).pack(pady=3)

tk.Button(root,
          text="Insert at End",
          width=25,
          command=insert_end).pack(pady=3)

tk.Button(root,
          text="Insert at Position",
          width=25,
          command=insert_position).pack(pady=3)

tk.Button(root,
          text="Delete by Value",
          width=25,
          command=delete_value).pack(pady=3)

tk.Button(root,
          text="Delete by Index",
          width=25,
          command=delete_index).pack(pady=3)

tk.Button(root,
          text="Display Linked List",
          width=25,
          command=show_list).pack(pady=3)

tk.Button(root,
          text="Clear",
          width=25,
          command=clear_boxes).pack(pady=3)

tk.Button(root,
          text="Exit",
          width=25,
          command=root.destroy).pack(pady=3)

tk.Label(root,
         text="Traversal",
         font=("Arial", 12, "bold")).pack(pady=10)

lbl_result = tk.Label(root,
                      text="Linked List is Empty",
                      font=("Arial", 12),
                      fg="blue",
                      wraplength=450)

lbl_result.pack()

root.mainloop()
