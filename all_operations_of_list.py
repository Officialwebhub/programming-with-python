# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)
# 1. Accessing elements
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])

# 2. Slicing the list
print("First 3 Elements:", my_list[:3])
print("Elements from index 2 onwards:", my_list[2:])

# 3. Adding elements
my_list.append(60)  # Append an element to the end of the list
print("After Appending 60:", my_list)

my_list.insert(2, 25)  # Insert 25 at index 2
print("After Inserting 25 at index 2:", my_list)

# 4. Removing elements
my_list.remove(40)  # Remove the first occurrence of 40
print("After Removing 40:", my_list)

popped_element = my_list.pop()  # Remove and return the last element
print("After Popping an Element:", my_list)
print("Popped Element:", popped_element)

my_list.pop(1)  # Remove the element at index 1
print("After Popping Element at Index 1:", my_list)

# 5. Modifying elements
my_list[2] = 35  # Modify the element at index 2
print("After Modifying Element at Index 2:", my_list)

# 6. Checking membership
print("Is 50 in the list?", 50 in my_list)
print("Is 100 in the list?", 100 in my_list)

# 7. Finding index of an element
index_of_30 = my_list.index(30)  # Find the index of the first occurrence of 30
print("Index of 30:", index_of_30)

# 8. Sorting the list
my_list.sort()  # Sort the list in ascending order
print("After Sorting:", my_list)

my_list.sort(reverse=True)  # Sort the list in descending order
print("After Sorting in Descending Order:", my_list)

# 9. Reversing the list
my_list.reverse()  # Reverse the order of elements
print("After Reversing:", my_list)

# 10. Copying a list
copied_list = my_list.copy()  # Create a shallow copy of the list
print("Copied List:", copied_list)

# 11. Clearing the list
my_list.clear()  # Remove all elements from the list
print("After Clearing the List:", my_list)

# 12. Length of the list
print("Length of Copied List:", len(copied_list))
