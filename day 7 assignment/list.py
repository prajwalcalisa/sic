import collections

# Create two linked lists using deque
linked_list1 = collections.deque()
linked_list2 = collections.deque()

# Input size of linked lists
n1 = int(input("Enter the number of elements in linked list 1: "))
n2 = int(input("Enter the number of elements in linked list 2: "))

# Input elements for linked list 1
print("Linked list 1:")
for i in range(n1):
    num = int(input("Enter the number: "))
    linked_list1.append(num)

# Input elements for linked list 2
print("Linked list 2:")
for i in range(n2):
    num = int(input("Enter the number: "))
    linked_list2.append(num)

# Display linked lists
print("Displaying linked list 1 elements:")
print(linked_list1)
print("Displaying linked list 2 elements:")
print(linked_list2)

# Check if both linked lists are converging (equal)
if set(linked_list1) & set(linked_list2):
    print("Both linked lists are converging.")
else:
    print("Both linked lists are not converging.")
