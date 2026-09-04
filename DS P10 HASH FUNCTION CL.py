# Practical 10: Hash Table

SIZE = 10
hash_table = [None] * SIZE

def insert(key, index):
    if hash_table[index] is None:
        hash_table[index] = key
        print("Key inserted successfully.")
    else:
        print("Index already occupied.")

def delete(index):
    if hash_table[index] is not None:
        hash_table[index] = None
        print("Key deleted successfully.")
    else:
        print("Index is empty.")

def search(key):
    for i in range(SIZE):
        if hash_table[i] == key:
            print("Key found at Index:", i)
            return
    print("Key not found.")

def traverse():
    print("\nIndex\tKey")
    for i in range(SIZE):
        print(i, "\t", hash_table[i])


# Menu
while True:
    print("\n--- HASH TABLE MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Traverse")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter Key Value: "))
        index = int(input("Enter Index No.: "))
        insert(key, index)

    elif choice == 2:
        index = int(input("Enter Index No. to delete: "))
        delete(index)

    elif choice == 3:
        key = int(input("Enter Key Value to search: "))
        search(key)

    elif choice == 4:
        traverse()

    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
