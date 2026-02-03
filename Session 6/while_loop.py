# while loop is a kind of loop that will continue to loop as long as a condition is met.

#ex:
count = 0
while count < 2:
    print("Count is:", count)
    count = count + 1  # Increment the count to avoid infinite loop
# you can also write like this count +=1

real_password = "Ali123"
password = ""
while password != real_password:
    password = input("Enter the password: ")
    if password == real_password:
        print("Access Granted")
    else:
        print("Access Denied, Try Again")