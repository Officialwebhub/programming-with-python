# Creating a string
my_string = "Hello, Python!"
print("Original String:", my_string)

# 1. Accessing characters
print("First Character:", my_string[0])
print("Last Character:", my_string[-1])

# 2. Slicing a string
print("First 5 Characters:", my_string[:5])
print("Characters from index 7 onwards:", my_string[7:])
print("Every 2nd Character:", my_string[::2])

# 3. String length
print("Length of String:", len(my_string))

# 4. Changing case
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Title Case:", my_string.title())

# 5. Checking for substrings
print("Does the string contain 'Python'? :", "Python" in my_string)
print("Does the string contain 'World'? :", "World" in my_string)

# 6. Removing whitespaces
my_string_with_spaces = "   Hello, Python!   "
print("Original with Whitespaces:", my_string_with_spaces)
print("After strip():", my_string_with_spaces.strip())  # Removes leading and trailing whitespaces
print("After lstrip():", my_string_with_spaces.lstrip())  # Removes leading whitespaces
print("After rstrip():", my_string_with_spaces.rstrip())  # Removes trailing whitespaces

# 7. Splitting and joining strings
words = my_string.split()  # Split the string into a list of words
print("Split String into List:", words)

joined_string = " ".join(words)  # Join the list of words back into a string
print("Joined String:", joined_string)

# 8. Replacing substrings
replaced_string = my_string.replace("Python", "World")
print("After Replacing 'Python' with 'World':", replaced_string)

# 9. String formatting
name = "Alice"
age = 25
formatted_string = f"My name is {name}, and I am {age} years old."
print("Formatted String:", formatted_string)

# 10. Finding substrings
index_of_P = my_string.find("P")  # Find the first occurrence of 'P'
print("Index of 'P':", index_of_P)

# 11. Count occurrences of a character or substring
count_l = my_string.count("l")
print("Count of 'l' in String:", count_l)

# 12. Checking the nature of the string
print("Is the string alphanumeric?:", my_string.isalnum())  # False due to punctuation and spaces
print("Is the string alphabetic?:", my_string.isalpha())  # False due to punctuation and spaces
print("Is the string numeric?:", my_string.isnumeric())  # False

# 13. Reversing a string
reversed_string = my_string[::-1]
print("Reversed String:", reversed_string)

# 14. Iterating through a string
print("Characters in the String:")
for char in my_string:
    print(char)

# 15. Copying strings
copied_string = my_string[:]
print("Copied String:", copied_string)
