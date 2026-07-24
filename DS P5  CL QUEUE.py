import time
import os


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
            print("Queue is full. Cannot enqueue.")
        else:
            self.queue.append(item)
            print(f"Enqueued: {item}")
        time.sleep(0.5)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        time.sleep(0.5)
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None

        print(f"Front of the queue: {self.queue[0]}")
        return self.queue[0]

    def traverse(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contains: ", end="")
            for item in self.queue:
                print(item, end=" ", flush=True)
                time.sleep(0.2)
            print()
        time.sleep(0.5)

    def display_list(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current Queue List:")
            for index, item in enumerate(self.queue):
                print(f"{index + 1}. {item}")
                time.sleep(0.2)
        time.sleep(0.5)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main Program
if __name__ == "__main__":

    max_size = int(input("Enter the maximum size of the queue: "))
    q = Queue(max_size)

    while True:
        clear_screen()

        print("\n===== Queue Operations Menu =====")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Traverse")
        print("5. Display List")
        print("6. Check if Queue is Empty")
        print("7. Check if Queue is Full")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            q.enqueue(item)

        elif choice == '2':
            q.dequeue()

        elif choice == '3':
            q.peek()

        elif choice == '4':
            q.traverse()

        elif choice == '5':
            q.display_list()

        elif choice == '6':
            if q.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")

        elif choice == '7':
            if q.is_full():
                print("Queue is full.")
            else:
                print("Queue is not full.")

        elif choice == '8':
            clear_screen()
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

        input("\nPress Enter to continue...")
