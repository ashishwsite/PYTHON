# Initialization
arr = [10, 20, 30, 40, 50]

# Accessing elements
print(arr[0])  # Output: 10

# Adding elements
arr.append(60)
arr.insert(2, 25)
arr.extend([70, 80])
print(arr)  # Output: [10, 20, 25, 30, 40, 50, 60, 70, 80]

# Removing elements
arr.remove(25)
arr.pop()
del arr[0]
print(arr)  # Output: [20, 30, 40, 50, 60, 70]

# Traversing
for elem in arr:
    print(elem)

# Sorting the list
arr.sort()
print(arr)  # Output: [20, 30, 40, 50, 60, 70]

# Reversing sort
arr.sort(reverse=True)
print(arr)  # Output: [70, 60, 50, 40, 30, 20]

# Slicing
print(arr[1:4])  # Output: [60, 50, 40]

# Length of the list
print(len(arr))  # Output: 6

# Checking if an element exists
print(50 in arr)  # Output: True

# Copying a list
copy_arr = arr.copy()
print(copy_arr)  # Output: [70, 60, 50, 40, 30, 20]
