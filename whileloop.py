"""
count = 0
height = 20
row = height

while count < height:
    print("*" * (count)  + " " * (row) + "*" * (count))
    count = count + 1
    row = row - 2


height = 20
count = range(0,height)
row = height

for i in count:
    for
    print("*" * (count[i])  + " " * (row) + "*" * (count[i]))
    row = row - 2
"""

# Function to demonstrate printing pattern triangle
def triangle(n):

    k = (2 * n) + 1

    for i in range(n, 0):
        for j in range(i + 1, 0):

      # printing stars
            print("*", end="")
    # inner loop to handle number spaces
    # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

    # decrementing k after each loop
        k = k + 2

    # inner loop to handle number of columns
    # values changing acc. to outer loop
        for j in range(i + 1, 0):

      # printing stars
            print("*", end="")

    # ending line after each row
        print("\r")


    # number of spaces
    k = (2 * n) - 1

    # outer loop to handle number of rows
    for i in range(0, n):

        for j in range(0, i+1):

          # printing stars
          print("*", end="")
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 2

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):

          # printing stars
          print("*", end="")

        # ending line after each row
        print("\r")

# Driver Code
n = 20
triangle(n)
