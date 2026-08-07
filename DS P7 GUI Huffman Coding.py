import tkinter as tk
from tkinter import messagebox
import heapq
from collections import Counter


class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encoding(data):
    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)

    encoded_data = "".join(codebook[ch] for ch in data)

    return encoded_data, codebook


def huffman_decoding(encoded_data, codebook):
    reverse = {v: k for k, v in codebook.items()}

    decoded = ""
    current = ""

    for bit in encoded_data:
        current += bit

        if current in reverse:
            decoded += reverse[current]
            current = ""

    return decoded


def encode():
    global codebook

    text = entry.get()

    if text == "":
        messagebox.showerror("Error", "Please enter text.")
        return

    encoded, codebook = huffman_encoding(text)

    encoded_var.set(encoded)
    codebook_var.set(str(codebook))


def decode():
    if encoded_var.get() == "":
        messagebox.showerror("Error", "Please encode first.")
        return

    decoded = huffman_decoding(encoded_var.get(), codebook)

    decoded_var.set(decoded)


root = tk.Tk()
root.title("Huffman Coding")
root.geometry("700x500")
root.config(bg="lightblue")

codebook = {}

tk.Label(root,
         text="Huffman Coding",
         font=("Arial", 18, "bold"),
         bg="lightblue").pack(pady=10)

tk.Label(root,
         text="Enter Text:",
         bg="lightblue",
         font=("Arial", 12)).pack()

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root,
          text="Encode",
          command=encode,
          bg="green",
          fg="white",
          width=15).pack(pady=5)

encoded_var = tk.StringVar()

tk.Label(root,
         text="Encoded Text:",
         bg="lightblue",
         font=("Arial", 12)).pack()

tk.Entry(root,
         textvariable=encoded_var,
         width=80).pack()

codebook_var = tk.StringVar()

tk.Label(root,
         text="Codebook:",
         bg="lightblue",
         font=("Arial", 12)).pack()

tk.Entry(root,
         textvariable=codebook_var,
         width=80).pack()

tk.Button(root,
          text="Decode",
          command=decode,
          bg="blue",
          fg="white",
          width=15).pack(pady=10)

decoded_var = tk.StringVar()

tk.Label(root,
         text="Decoded Text:",
         bg="lightblue",
         font=("Arial", 12)).pack()

tk.Entry(root,
         textvariable=decoded_var,
         width=80).pack()

tk.Button(root,
          text="Exit",
          command=root.destroy,
          bg="red",
          fg="white",
          width=15).pack(pady=20)

root.mainloop()
