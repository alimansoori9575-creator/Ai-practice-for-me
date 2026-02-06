# A function is a code that runs when you call it.
#ex:
def greet():
    print("Hello, welcome to the world of functions!")
greet()  # This will call the function and execute the code inside it.

# parameters and arguments

def greet(name): # name is a parameter which is empty now like a variable, we will fill it when we call the function
    print("Hello, " , name)
greet("Ali") # Ali is an argument which is the value we are passing to the function, it will replace the parameter name when we call the function
greet("Sara") # we can call the same function with different arguments to get different outputs

# you can also have multiple parameters in a function
# some experiments with multiple parameters and arguments

def greet(name, age):
    print(f"Hello, {name} you are {age} years old.")
greet(str(input("Enter your name: ")), int(input("Enter your age: "))) # we can pass multiple arguments to the function, they will replace the parameters in the order they are defined

# calculate the price of a product whose unit price is 300rs and quantity is 3

def total_price(unit_price, quantity):
    total = unit_price * quantity
    print(f"The total price is: {total} rs")
total_price(300, 3) 