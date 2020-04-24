import time
from binary_search_tree import BinarySearchTree  # <- add and import BST file

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Use a binary search tree
# BST list 1
# iterate through names on list 2 to compare them to list 1
# if the name is on both list 2 and list 1 append the name to a duplicates list

binary_tree = BinarySearchTree('names')

for names in names_1:  # binary search tree
    binary_tree.insert(names)  # made of names from names_1 list

for name in names_2:  # find duplicates
    # if the name from names_2 list is also a name in names_1 list
    if binary_tree.contains(name):
        duplicates.append(name)  # append to duplicates list

end_time = time.time()
print(f"\n{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds \n")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
