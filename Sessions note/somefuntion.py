# print is a function that outputs data to the console
print("Hello, World!")  # Output: Hello, World! 
# You can print different data types
print(42)               # Output: 42 (integer)
# ex:
a = 10
print(a + 5)  # Output: 15
# some experiments with print function
print("The value of a is:", a)  # Output: The value of a is: 10
# you can do that in this way too without comma
print(f"The value of a is: {a}")  # Output: The value of a is: 10

### input() function:
# input() function allows user to take input from the user  
name = input("Enter your name: ")  # Prompts user to enter their name
print("Hello, " + name + "!")  
age = input("Enter your age: ")  # Prompts user to enter their age
print(f"age of {name} is: {age}")