import tkinter as tk
from tkinter import messagebox

SIZE = 10
hash_table = [None] * SIZE


def insert():
    try:
        key = int(key_entry.get())
        index = int(index_entry.get())

        if index < 0 or index >= SIZE:
            messagebox.showerror("Error", "Index must be between 0 and 9")
            return

        if hash_table[index] is None:
            hash_table[index] = key
            messagebox.showinfo("Success",
                                f"Key {key} inserted at Index {index}")
            key_entry.delete(0, tk.END)
            index_entry.delete(0, tk.END)
            traverse()
        else:
            messagebox.showwarning("Warning", "Index already occupied!")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")


def delete():
    try:
        index = int(index_entry.get())

        if index < 0 or index >= SIZE:
            messagebox.showerror("Error", "Index must be between 0 and 9")
            return

        if hash_table[index] is not None:
            key = hash_table[index]
            hash_table[index] = None
            messagebox.showinfo("Success",
                                f"Key {key} deleted from Index {index}")
            index_entry.delete(0, tk.END)
            traverse()
        else:
            messagebox.showwarning("Warning", "Index is empty!")

    except ValueError:
        messagebox.showerror("Error", "Enter valid Index")


def search():
    try:
        key = int(key_entry.get())

        for i in range(SIZE):
            if hash_table[i] == key:
                messagebox.showinfo("Search Result",
                                    f"Key {key} found at Index {i}")
                return

        messagebox.showwarning("Search Result",
                               f"Key {key} not found")

    except ValueError:
        messagebox.showerror("Error", "Enter valid Key")


def traverse():
    for i in range(SIZE):
        if hash_table[i] is None:
            table_labels[i].config(text=f"Index {i} : Empty")
        else:
            table_labels[i].config(
                text=f"Index {i} : {hash_table[i]}"
            )


def exit_program():
    root.destroy()


root = tk.Tk()
root.title("Hash Table")
root.geometry("500x600")
root.resizable(False, False)

title = tk.Label(
    root,
    text="HASH TABLE",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)


tk.Label(
    root,
    text="Key Value:",
    font=("Arial", 12)
).pack()

key_entry = tk.Entry(root, font=("Arial", 12), width=25)
key_entry.pack(pady=5)


tk.Label(
    root,
    text="Index No. (0-9):",
    font=("Arial", 12)
).pack()

index_entry = tk.Entry(root, font=("Arial", 12), width=25)
index_entry.pack(pady=5)



tk.Button(
    root,
    text="INSERT",
    width=18,
    command=insert
).pack(pady=7)

tk.Button(
    root,
    text="DELETE",
    width=18,
    command=delete
).pack(pady=7)

tk.Button(
    root,
    text="SEARCH",
    width=18,
    command=search
).pack(pady=7)

tk.Button(
    root,
    text="TRAVERSE",
    width=18,
    command=traverse
).pack(pady=7)

tk.Button(
    root,
    text="EXIT",
    width=18,
    command=exit_program
).pack(pady=7)



tk.Label(
    root,
    text="Hash Table",
    font=("Arial", 16, "bold")
).pack(pady=15)

table_labels = []

for i in range(SIZE):
    label = tk.Label(
        root,
        text=f"Index {i} : Empty",
        font=("Arial", 11)
    )
    label.pack()
    table_labels.append(label)


root.mainloop()
