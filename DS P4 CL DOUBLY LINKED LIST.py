import time

# Node 
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


#Doubly Linked List 
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at Position
    def insert_at_position(self, data, position):

        if position < 0:
            raise IndexError("Invalid Position")

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(position):
            if temp is None:
                raise IndexError("Position Out of Bounds")
            temp = temp.next

        if temp is None:
            self.insert_at_end(data)
            return

        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node

    # Delete at Beginning
    def delete_at_beginning(self):

        if self.head is None:
            print("List is Empty.")
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Delete at End
    def delete_at_end(self):

        if self.head is None:
            print("List is Empty.")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # Delete at Position
    def delete_at_position(self, position):

        if self.head is None:
            raise IndexError("List is Empty")

        if position == 0:
            self.delete_at_beginning()
            return

        temp = self.head

        for i in range(position):
            if temp is None:
                raise IndexError("Invalid Position")
            temp = temp.next

        if temp is None:
            raise IndexError("Invalid Position")

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    # Search
    def search(self, key):

        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    # Length
    def length(self):

        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # Display
    def display(self):

        if self.head is None:
            print("Doubly Linked List is Empty.")
            return

        temp = self.head

        print("\nDoubly Linked List : ", end="")

        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next

        print()


def menu():

    print("\n========== DOUBLY LINKED LIST ==========")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Position")
    print("7. Display List")
    print("8. Search Node")
    print("9. Length of List")
    print("10. Exit")

def main():

    dll = DoublyLinkedList()

    while True:

        menu()

        try:

            choice = int(input("Enter your choice : "))

            if choice == 1:

                data = int(input("Enter Data : "))
                dll.insert_at_beginning(data)
                print("Node Inserted Successfully.")

            elif choice == 2:

                data = int(input("Enter Data : "))
                dll.insert_at_end(data)
                print("Node Inserted Successfully.")

            elif choice == 3:

                data = int(input("Enter Data : "))
                pos = int(input("Enter Position : "))
                dll.insert_at_position(data, pos)
                print("Node Inserted Successfully.")

            elif choice == 4:

                dll.delete_at_beginning()
                print("Node Deleted from Beginning.")

            elif choice == 5:

                dll.delete_at_end()
                print("Node Deleted from End.")

            elif choice == 6:

                pos = int(input("Enter Position : "))
                dll.delete_at_position(pos)
                print("Node Deleted Successfully.")

            elif choice == 7:

                dll.display()

            elif choice == 8:

                key = int(input("Enter Data to Search : "))

                if dll.search(key):
                    print("Node Found.")
                else:
                    print("Node Not Found.")

            elif choice == 9:

                print("Length of List :", dll.length())

            elif choice == 10:

                print("Exiting Program...")
                break

            else:

                print("Invalid Choice.")

        except ValueError:
            print("Please Enter Valid Integer.")

        except IndexError as e:
            print("Error :", e)

        except Exception as e:
            print("Unexpected Error :", e)

        time.sleep(1)


if __name__ == "__main__":
    main()
