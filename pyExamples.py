# For loop to iterate over a range of numbers
for i in range(5):
    print(i)

# While loop that runs until a condition is met
count = 0
while count < 5:
    print(count)
    count += 1

# Creating and manipulating a list
my_list = [1, 2, 3, 4, 5]

# Accessing list elements
print(my_list[0])  # Output: 1

# Modifying list elements
my_list[0] = 10
my_list[5] = 10

# Looping through a list
for element in my_list:
    print(element)

# Adding an element to the list
my_list.append(6)

# Output the modified list
print(my_list)

x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

# Taking user input
name = input("Enter your name: ")

# Outputting a message
print("Hello, " + name + "!")

my_list = [1, 2, 3]
print(my_list[0])
my_list.append(4)

if x > 10: print("Greater")
elif x == 10: print("Equal")
else: print("Less")

for i in range(5):
    print(i)

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Looping over keys
for key in my_dict:
    print(key)

# Looping over keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Create a list of squares using list comprehension
squares = [x**2 for x in range(5)]
print(squares)

for i in range(40):
    if i % 3 == 0:
        print("fizz", end="")
    if i % 5 == 0:
        print("buzz", end="")
    if i % 3 != 0 and i % 5 != 0:
        print(i, end="")
    print("")
