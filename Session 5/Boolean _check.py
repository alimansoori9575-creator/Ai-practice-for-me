user_logged_in = True
user_has_premium = False

if user_logged_in: # you can also use "if user_logged_in == True:"
    print("Welcome back, user!")


if user_logged_in and user_has_premium:
    print("Access granted to premium content.")
else:
    print("Access denied. Please log in and/or upgrade to premium.")

###         Boolean check in Python         ###
atm_pin = 1234
entered_pin = 1111 # pin accepted or pin wrong
if entered_pin == atm_pin: # or if entered_pin == 1234:
    print("Pin accepted. You can proceed with your transaction.")
else:
    print("Wrong pin. Please try again.")

    