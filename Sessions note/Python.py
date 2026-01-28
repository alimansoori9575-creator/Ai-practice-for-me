## 1.Variables means labels that are used to store data values.
## ex: age = 5
##python variables:
#must start with a letter or an underscore(_)
#cannot start with a number
#can contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#variables are case-sensitive (age, Age and AGE are three different variables)

## 2. Data Types:
#Common data types in Python include:
#int: Integer numbers (e.g., 5, -3, 42)
#float: Floating point numbers (e.g., 3.14, -2.5)
#str: Strings latters (e.g., "Hello", 'Python')
#bool: Boolean values (True or False)

####     some experiments with variables and data types   ####
message = " Hello, how are you?"
name = "ali"
is_active = True
is_dead = False 
print(type(is_active))  # Output: <class 'bool'>
human = "hello " + name + message
print(human)          