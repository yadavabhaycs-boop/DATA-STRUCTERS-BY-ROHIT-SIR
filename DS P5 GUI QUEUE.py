import tkinter as tk
from tkinter import messagebox


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return False
        self.queue.append(item)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]


# Create Queue
max_size = 5
q = Queue(max_size)


# Functions
def enqueue():
    item = entry.get()
    if item == "":
        messagebox.showwarning("Warning", "Enter a value.")
        return

    if q.enqueue(item):
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Queue is Full!")


def dequeue():
    item = q.dequeue()
    if item is None:
        messagebox.showerror("Error", "Queue is Empty!")
    else:
        messagebox.showinfo("Dequeued", f"Removed: {item}")
        update_listbox()


def peek():
    item = q.peek()
    if item is None:
        messagebox.showinfo("Peek", "Queue is Empty!")
    else:
        messagebox.showinfo("Peek", f"Front Element: {item}")


def check_empty():
    if q.is_empty():
        messagebox.showinfo("Status", "Queue is Empty")
    else:
        messagebox.showinfo("Status", "Queue is Not Empty")


def check_full():
    if q.is_full():
        messagebox.showinfo("Status", "Queue is Full")
    else:
        messagebox.showinfo("Status", "Queue is Not Full")


def update_listbox():
    listbox.delete(0, tk.END)
    for item in q.queue:
        listbox.insert(tk.END, item)


# GUI Window
root = tk.Tk()
root.title("Queue Operations")
root.geometry("400x450")

tk.Label(root, text="Queue GUI", font=("Arial", 16, "bold")).pack(pady=10)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

tk.Button(root, text="Enqueue", width=20, command=enqueue).pack(pady=3)
tk.Button(root, text="Dequeue", width=20, command=dequeue).pack(pady=3)
tk.Button(root, text="Peek", width=20, command=peek).pack(pady=3)
tk.Button(root, text="Check Empty", width=20, command=check_empty).pack(pady=3)
tk.Button(root, text="Check Full", width=20, command=check_full).pack(pady=3)

tk.Label(root, text="Queue Elements").pack(pady=5)

listbox = tk.Listbox(root, width=35, height=10)
listbox.pack(pady=5)

tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=10)

root.mainloop()
