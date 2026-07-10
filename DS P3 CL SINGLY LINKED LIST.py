import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    # Insert at Position
    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        new_node.next = temp.next
        temp.next = new_node

    # Delete by Value
    def delete_node_by_value(self, key):
        temp = self.head

        if temp is None:
            return False

        if temp.data == key:
            self.head = temp.next
            return True

        prev = None

        while temp is not None:
            if temp.data == key:
                prev.next = temp.next
                return True

            prev = temp
            temp = temp.next

        return False

    # Delete by Index
    def delete_node_by_index(self, position):

        if self.head is None:
            raise IndexError("Linked List is Empty.")

        if position == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None or temp.next is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        temp.next = temp.next.next

    # Display
    def display_list(self):

        temp = self.head

        if temp is None:
            print("\nLinked List is Empty.")
            return

        print("\nLinked List : ", end="")

        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next

        print()



def display_menu():

    print("\n========== SINGLY LINKED LIST ==========")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete Node by Value")
    print("5. Delete Node by Index")
    print("6. Display Linked List")
    print("7. Exit")



def main():

    linked_list = LinkedList()

    while True:

        display_menu()

        try:

            choice = int(input("Enter your choice : "))

            if choice == 1:

                data = int(input("Enter data : "))
                linked_list.insert_at_beginning(data)
                print("Node inserted at beginning.")

            elif choice == 2:

                data = int(input("Enter data : "))
                linked_list.insert_at_end(data)
                print("Node inserted at end.")

            elif choice == 3:

                data = int(input("Enter data : "))
                position = int(input("Enter position : "))

                linked_list.insert_at_position(data, position)
                print("Node inserted successfully.")

            elif choice == 4:

                value = int(input("Enter value to delete : "))

                if linked_list.delete_node_by_value(value):
                    print("Node deleted successfully.")
                else:
                    print("Value not found.")

            elif choice == 5:

                position = int(input("Enter index to delete : "))
                linked_list.delete_node_by_index(position)
                print("Node deleted successfully.")

            elif choice == 6:

                linked_list.display_list()

            elif choice == 7:

                print("Exiting Program...")
                break

            else:

                print("Invalid Choice.")

        except ValueError:
            print("Please enter valid integer values.")

        except IndexError as e:
            print("Error:", e)

        except Exception as e:
            print("Unexpected Error:", e)

        time.sleep(1)


if __name__ == "__main__":
    main()
