#S123 ABHAY YADAV
import os
import time
from termcolor import colored, cprint


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        cprint(f"'{item}' has been pushed onto the stack.", "green")
        self.animate_push(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop.")

        item = self.items.pop()
        cprint(f"'{item}' has been popped from the stack.", "red")
        self.animate_pop(item)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek.")

        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        if self.is_empty():
            return "Stack is Empty"
        return " <- ".join(reversed(self.items))

    def animate_push(self, item):
        for _ in range(3):
            print(colored(f"Pushing {item}...", "yellow"))
            time.sleep(0.3)
            self.clear_screen()

    def animate_pop(self, item):
        for _ in range(3):
            print(colored(f"Popping {item}...", "magenta"))
            time.sleep(0.3)
            self.clear_screen()

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def stack_operations():
    stack = Stack()

    cprint("=" * 50, "cyan")
    cprint("      INTERACTIVE STACK OPERATIONS", "cyan", attrs=["bold"])
    cprint("=" * 50, "cyan")

    while True:
        print("\nCurrent Stack:", colored(str(stack), "blue"))

        print(colored("\n1. Push Element", "yellow"))
        print(colored("2. Pop Element", "yellow"))
        print(colored("3. Peek Element", "yellow"))
        print(colored("4. Check if Stack is Empty", "yellow"))
        print(colored("5. Stack Size", "yellow"))
        print(colored("6. Exit", "yellow"))

        try:
            choice = int(input(colored("\nEnter your choice (1-6): ", "green")))
        except ValueError:
            cprint("Please enter a valid number.", "red")
            continue

        if choice == 1:
            item = input(colored("Enter element to push: ", "green"))
            stack.push(item)

        elif choice == 2:
            try:
                stack.pop()
            except IndexError as e:
                cprint(e, "red")

        elif choice == 3:
            try:
                cprint(f"Top Element: {stack.peek()}", "blue")
            except IndexError as e:
                cprint(e, "red")

        elif choice == 4:
            if stack.is_empty():
                cprint("Stack is Empty.", "blue")
            else:
                cprint("Stack is Not Empty.", "blue")

        elif choice == 5:
            cprint(f"Stack Size: {stack.size()}", "blue")

        elif choice == 6:
            cprint("\nThank you for using the Stack Program!", "cyan", attrs=["bold"])
            break

        else:
            cprint("Invalid Choice! Enter a number between 1 and 6.", "red")


if __name__ == "__main__":
    stack_operations()
