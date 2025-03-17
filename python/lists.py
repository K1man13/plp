# printig list of items in a shopping cart

fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Outputs: apple

# Modifying an element
fruits[1] = "orange"
print(fruits)  # Outputs: ['apple', 'orange', 'cherry']

# Adding an element
fruits.append("grape")
print(fruits)  # Outputs: ['apple', 'orange', 'cherry', 'grape']






# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend the list with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)
