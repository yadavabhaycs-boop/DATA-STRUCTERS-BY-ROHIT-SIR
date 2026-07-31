import tkinter as tk
from tkinter import messagebox, ttk


class PriorityQueueGUI:

  def __init__(self, root):
    self.root = root
    self.root.title("Priority Queue Visualizer")
    self.root.geometry("500x600")
    self.root.resizable(False, False)

    self.queue = []
    self.max_capacity = 5

    self.setup_ui()

  def setup_ui(self):
    # Styling
    style = ttk.Style()
    style.theme_use("clam")

    # Header Frame (Capacity Setting)
    cap_frame = ttk.LabelFrame(self.root, text=" Configuration ", padding=10)
    cap_frame.pack(fill="x", padx=15, pady=10)

    ttk.Label(cap_frame, text="Max Capacity:").grid(
        row=0, column=0, padx=5, sticky="w"
    )
    self.cap_entry = ttk.Entry(cap_frame, width=10)
    self.cap_entry.insert(0, str(self.max_capacity))
    self.cap_entry.grid(row=0, column=1, padx=5)

    ttk.Button(cap_frame, text="Set Capacity", command=self.set_capacity).grid(
        row=0, column=2, padx=5
    )

    # Input Frame (Enqueue Options)
    input_frame = ttk.LabelFrame(
        self.root, text=" Enqueue / Dequeue Operations ", padding=10
    )
    input_frame.pack(fill="x", padx=15, pady=5)

    ttk.Label(input_frame, text="Item Name:").grid(
        row=0, column=0, padx=5, pady=5, sticky="w"
    )
    self.item_entry = ttk.Entry(input_frame, width=15)
    self.item_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(input_frame, text="Priority (int):").grid(
        row=1, column=0, padx=5, pady=5, sticky="w"
    )
    self.priority_entry = ttk.Entry(input_frame, width=15)
    self.priority_entry.grid(row=1, column=1, padx=5, pady=5)

    btn_enqueue = ttk.Button(
        input_frame, text="Enqueue", command=self.enqueue_item
    )
    btn_enqueue.grid(row=0, column=2, padx=10, pady=5)

    btn_dequeue = ttk.Button(
        input_frame, text="Dequeue", command=self.dequeue_item
    )
    btn_dequeue.grid(row=1, column=2, padx=10, pady=5)

    # Display Options Frame
    display_frame = ttk.LabelFrame(self.root, text=" View Options ", padding=10)
    display_frame.pack(fill="x", padx=15, pady=5)

    ttk.Button(
        display_frame, text="Show Current Queue", command=self.show_queue
    ).pack(side="left", expand=True, padx=5)
    ttk.Button(
        display_frame,
        text="Ascending Order",
        command=self.show_ascending,
    ).pack(side="left", expand=True, padx=5)
    ttk.Button(
        display_frame,
        text="Descending Order",
        command=self.show_descending,
    ).pack(side="left", expand=True, padx=5)

    # Status Indicators
    status_frame = ttk.Frame(self.root, padding=5)
    status_frame.pack(fill="x", padx=15, pady=5)

    ttk.Button(
        status_frame, text="Check Empty / Full", command=self.check_status
    ).pack(side="left")
    self.status_label = ttk.Label(
        status_frame, text="Status: Ready", font=("Arial", 9, "italic")
    )
    self.status_label.pack(side="right", padx=10)

    # Listbox Display Area
    list_frame = ttk.LabelFrame(self.root, text=" Queue State ", padding=10)
    list_frame.pack(fill="both", expand=True, padx=15, pady=10)

    self.tree = ttk.Treeview(
        list_frame, columns=("Item", "Priority"), show="headings"
    )
    self.tree.heading("Item", text="Item Name")
    self.tree.heading("Priority", text="Priority Level")
    self.tree.column("Item", anchor="center")
    self.tree.column("Priority", anchor="center")
    self.tree.pack(fill="both", expand=True)

  # Core Logic Methods
  def set_capacity(self):
    try:
      val = int(self.cap_entry.get().strip())
      if val <= 0:
        raise ValueError
      self.max_capacity = val
      messagebox.showinfo(
          "Success", f"Maximum capacity set to {self.max_capacity}."
      )
      self.update_status()
    except ValueError:
      messagebox.showerror(
          "Error", "Please enter a valid positive integer for capacity."
      )

  def enqueue_item(self):
    if len(self.queue) >= self.max_capacity:
      messagebox.showwarning(
          "Full", "Priority Queue is full. Cannot enqueue item."
      )
      return

    item = self.item_entry.get().strip()
    priority_str = self.priority_entry.get().strip()

    if not item:
      messagebox.showerror("Error", "Item name cannot be empty.")
      return

    try:
      priority = int(priority_str)
    except ValueError:
      messagebox.showerror(
          "Error", "Priority must be an integer (e.g., 1, 2, 3)."
      )
      return

    self.queue.append((item, priority))
    self.queue.sort(key=lambda x: x[1])  # Sort by priority

    self.item_entry.delete(0, tk.END)
    self.priority_entry.delete(0, tk.END)

    self.show_queue()
    self.update_status()
    messagebox.showinfo("Enqueued", f"Added '{item}' with priority {priority}.")

  def dequeue_item(self):
    if not self.queue:
      messagebox.showwarning(
          "Empty", "Priority Queue is empty. Cannot dequeue."
      )
      return

    item, priority = self.queue.pop(0)
    self.show_queue()
    self.update_status()
    messagebox.showinfo(
        "Dequeued",
        f"Dequeued highest priority item: '{item}' (Priority {priority}).",
    )

  def show_queue(self):
    self.clear_tree()
    for item, priority in self.queue:
      self.tree.insert("", "end", values=(item, priority))

  def show_ascending(self):
    self.clear_tree()
    sorted_q = sorted(self.queue, key=lambda x: x[1])
    for item, priority in sorted_q:
      self.tree.insert("", "end", values=(item, priority))

  def show_descending(self):
    self.clear_tree()
    sorted_q = sorted(self.queue, key=lambda x: x[1], reverse=True)
    for item, priority in sorted_q:
      self.tree.insert("", "end", values=(item, priority))

  def check_status(self):
    is_empty = len(self.queue) == 0
    is_full = len(self.queue) >= self.max_capacity

    msg = f"Queue Size: {len(self.queue)}/{self.max_capacity}\n"
    msg += f"Is Empty: {'Yes' if is_empty else 'No'}\n"
    msg += f"Is Full: {'Yes' if is_full else 'No'}"

    messagebox.showinfo("Queue Status", msg)

  def update_status(self):
    self.status_label.config(
        text=f"Items: {len(self.queue)}/{self.max_capacity}"
    )

  def clear_tree(self):
    for row in self.tree.get_children():
      self.tree.delete(row)


if __name__ == "__main__":
  root = tk.Tk()
  app = PriorityQueueGUI(root)
  root.mainloop()