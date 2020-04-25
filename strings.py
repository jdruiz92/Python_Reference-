# Strings
print("Strings")

# creates a string
Name = "Daniel Ruiz"

# prints string
print("1. The string is " + Name)

# print the first element in the string
print("2. The first element in " + Name + " is " + Name[0])

# print element on index 6
print("3. The seventh element in " + Name + " is " + Name[7])

# prints element on last index
print("4. The last element in " + Name + " is " + Name[-1])

# prints first element on first index
print("5. The first element in " + Name + " is " + Name[-11])

# find the length of the number of characters in a string
print("6. The length of the string is " + str(len(Name)) + "\n")


# Slicing
print("Slicing")

# Take the slice on variable Name with only index 0 to index 3
print("1. index 0 to 3 is " + Name[0:4])

# Take the slice on variable Name with only index 7 to index 10
print("2. index 7 to 10 is " + Name[7:10])
print("\n")


# Stride
print("Stride")

# Get every second element. The elments on index 1, 3, 5 ...
print("1. Every second element of my name is " + Name[::2])

# Get every second element in the range from index 0 to index 4
print("2. Every second element from index 0 to 4 is " + Name[0:5:2])
print("\n")

# Concatenation
print("Concatenate")

# Concatenate two strings
Statement = Name + " is the best"
print("1. " + Statement)

# Print string three times
print("2. " + (Name + " ") * 3)

# Concatenate Strings
Name = "Daniel Ruiz"
Name = Name + " is the best"
print("3. " + Name)
print("\n")


# Escape Sequences
print("Escape Sequences")

# New line escape sequence
print("1. Daniel Ruiz \n is the best")

# Tab escape sequence
print("2. Daniel Ruiz\t is the best")

# Include back slash in string
print("3. Daniel Ruiz \\ is the best")

# r will tell python that string will be display as raw string
print(r"4. Daniel Ruiz \ is the best")
print("\n")

# String Operations
print("String Operations")

# Convert all the characters in string to upper case
A = "I look forward to my career as a programmer"
print("1. before upper:", A)

B = A.upper()
print("2. After upper:", B)

# Replace the old substring with the new target substring is
# the segment has been found in the string

A = "Daniel Ruiz is the best"
B = A.replace('Daniel' , 'Sammuel')
print("3. Replace operations:", B)

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
el = Name.find('el')
print("4. The index of first element of 'el' is ", el)

# Find the substring in the string
lastname = Name.find('Ruiz')
print("5. The index of first element of 'Ruiz' is", lastname)

# If cannot find the substring in the string
nosubstr = Name.find('Jasdfasdasdf')
print("6. When substring cannot be found", nosubstr)
