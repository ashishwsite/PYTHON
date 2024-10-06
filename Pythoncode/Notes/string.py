# Initialization
s = "Hello World"

# Accessing
print(s[0])  # Output: H
print(s[-1])  # Output: d

# Traversal
for char in s:
    print(char)

# Slicing
print(s[0:5])  # Output: Hello
print(s[-5:])  # Output: World

# Concatenation
s2 = "Python"
s3 = s + " " + s2
print(s3)  # Output: Hello World Python

# Length
print(len(s))  # Output: 11

# Searching
print(s.find("World"))  # Output: 6
print(s.startswith("Hell"))  # Output: True

# Case conversion
print(s.upper())  # Output: HELLO WORLD
print(s.lower())  # Output: hello world

# Splitting and joining
words = s.split()
print(words)  # Output: ['Hello', 'World']
joined_string = ' '.join(words)
print(joined_string)  # Output: Hello World

# Sorting characters
sorted_string = ''.join(sorted(s))
print(sorted_string)  # Output:  HWdellloor

# Checking substring
print("World" in s)  # Output: True

# Formatting
age = 25
formatted_string = f"I am {age} years old."
print(formatted_string)  # Output: I am 25 years old.
