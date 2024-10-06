# Initialization of sets
my_set = {1, 2, 3}
another_set = set([3, 4, 5])
t_set=set()

# Adding elements
my_set.add(4)  # Add a single element
my_set.update([5, 6])  # Add multiple elements

# Removing elements
my_set.remove(6)  # Removes 6 (raises error if not found)
my_set.discard(10)  # Safe remove, doesn't raise error if not found

# Traversing the set
for elem in my_set:
    print(f"Element: {elem}")

# Sorting a set (returns a sorted list, not a set)
sorted_list = sorted(my_set)
print(f"Sorted set: {sorted_list}")

# Union of sets
union_set = my_set | another_set
print(f"Union: {union_set}")

# Intersection of sets
intersection_set = my_set & another_set
print(f"Intersection: {intersection_set}")

# Difference of sets
difference_set = my_set - another_set
print(f"Difference: {difference_set}")

# Symmetric Difference of sets
symmetric_difference_set = my_set ^ another_set
print(f"Symmetric Difference: {symmetric_difference_set}")

# Checking membership
print(3 in my_set)  # True
print(7 in my_set)  # False

# Length of the set
print(f"Length of the set: {len(my_set)}")

# Copying the set
copied_set = my_set.copy()
print(f"Copied set: {copied_set}")

# Clearing the set
my_set.clear()
print(f"Set after clearing: {my_set}")
