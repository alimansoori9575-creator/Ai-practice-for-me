####        use of logical operaters in python       ####
# use of and operator
age = 20
has_address = True
if age >= 18 and has_address:
    print("Entry allowed.")
else:
    print("Entry denied.")

balance = 500
price = 300
is_user_account_exist = True
if balance >= price and price > 0 and is_user_account_exist:
    print("Purchase successful.")
else:
    print("Purchase failed.")


# use of or operator

user_human = True   
user_robot = False
if user_robot or user_human:
    print("User verified.") 
else:
    print("User not verified.")

is_owner = True
is_admin = False
if is_owner or is_admin:
    print("Access granted.")  
else:
    print("Access denied.")

coin = 200
voucher = 300
item_price = 120
if coin >= item_price or voucher >= item_price:
    print("Item can be purchased through", "coin." if coin >= item_price else "voucher.")
else:
    print("Insufficient funds.")

# use of not operator
is_raining = False 
if not is_raining:
    print("It's a sunny day.")
else:
    print("It's raining.")

completed = False
if not completed:
    print("Task is complete.")