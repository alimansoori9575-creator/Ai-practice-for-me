# name, age, phone

user = {
    "name": "Ali",
    "age": "21",
    "phone": "1234567",
    "valid_user": False
}
print(user)
print(user["name"])

#add a new key
user["email"] = 'ali@gmail.com'
print(user['email'])

#get it in loop
for i in user.items():
    print(i)

for i, j in user.items():
    if i == "valid_user" and j == False:
        print("Invalid user")


