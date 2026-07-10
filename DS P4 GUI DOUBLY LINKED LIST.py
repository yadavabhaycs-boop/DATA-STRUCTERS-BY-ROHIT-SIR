
import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)
        if self.head:
            new.next = self.head
            self.head.prev = new
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def insert_position(self, data, pos):
        if pos < 0:
            raise IndexError("Invalid Position")
        if pos == 0:
            self.insert_begin(data)
            return
        temp = self.head
        i = 0
        while temp and i < pos - 1:
            temp = temp.next
            i += 1
        if temp is None:
            raise IndexError("Invalid Position")
        if temp.next is None:
            self.insert_end(data)
            return
        new = Node(data)
        new.next = temp.next
        new.prev = temp
        temp.next.prev = new
        temp.next = new

    def delete_begin(self):
        if self.head is None:
            raise IndexError("List Empty")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            raise IndexError("List Empty")
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_position(self, pos):
        if pos < 0:
            raise IndexError("Invalid Position")
        if self.head is None:
            raise IndexError("List Empty")
        if pos == 0:
            self.delete_begin()
            return
        temp = self.head
        i = 0
        while temp and i < pos:
            temp = temp.next
            i += 1
        if temp is None:
            raise IndexError("Invalid Position")
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def search(self, value):
        t = self.head
        while t:
            if t.data == value:
                return True
            t = t.next
        return False

    def length(self):
        c = 0
        t = self.head
        while t:
            c += 1
            t = t.next
        return c

    def display(self):
        if self.head is None:
            return "Doubly Linked List is Empty"
        s = []
        t = self.head
        while t:
            s.append(str(t.data))
            t = t.next
        return " <-> ".join(s)

dll = DoublyLinkedList()

def refresh():
    lbl.config(text=dll.display())

def get_data():
    return int(data_entry.get())

def get_pos():
    return int(pos_entry.get())

def safe(fn):
    try:
        fn()
        refresh()
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Doubly Linked List")
root.geometry("500x560")
root.resizable(False, False)

tk.Label(root,text="DOUBLY LINKED LIST",font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root,text="Data").pack()
data_entry=tk.Entry(root,width=30)
data_entry.pack()

tk.Label(root,text="Position").pack()
pos_entry=tk.Entry(root,width=30)
pos_entry.pack()

buttons = [
("Insert Beginning", lambda: safe(lambda: dll.insert_begin(get_data()))),
("Insert End", lambda: safe(lambda: dll.insert_end(get_data()))),
("Insert Position", lambda: safe(lambda: dll.insert_position(get_data(), get_pos()))),
("Delete Beginning", lambda: safe(dll.delete_begin)),
("Delete End", lambda: safe(dll.delete_end)),
("Delete Position", lambda: safe(lambda: dll.delete_position(get_pos()))),
("Search", lambda: messagebox.showinfo("Search","Node Found" if dll.search(get_data()) else "Node Not Found")),
("Length", lambda: messagebox.showinfo("Length",str(dll.length()))),
("Display", refresh),
("Clear", lambda:(data_entry.delete(0,tk.END),pos_entry.delete(0,tk.END))),
("Exit", root.destroy)
]

for text,cmd in buttons:
    tk.Button(root,text=text,width=25,command=cmd).pack(pady=3)

lbl=tk.Label(root,text="Doubly Linked List is Empty",font=("Arial",12),fg="blue",wraplength=450)
lbl.pack(pady=20)

root.mainloop()
