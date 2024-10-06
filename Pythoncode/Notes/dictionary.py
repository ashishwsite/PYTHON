# Initialization
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Adding and updating
my_dict['country'] = 'USA'
my_dict['age'] = 26

# Removing
my_dict.pop('city')
del my_dict['country']

# Traversing
for key, value in my_dict.items():
    print(f'{key}: {value}')
    print(value)

# Sorting
sorted_by_keys = dict(sorted(my_dict.items()))  # Sort by keys
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))  # Sort by values

# Merging
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2  # Merge dictionaries (Python 3.9+)

# Check if key exists
print('name' in my_dict)  # True

# Copying
copy_dict = my_dict.copy()
