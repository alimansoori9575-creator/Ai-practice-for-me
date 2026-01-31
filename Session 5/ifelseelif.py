###         if, else, elif statements in Python         ###

age = 20

if age >= 18:
    print("You are eligible to vote.")

marks = 50

if marks >= 40:
    print("Pass")
else:
    print("Fail")

tamperature = 40

if tamperature > 30:
    print("Hot day") 
elif tamperature < 15:
    print("Cold day")
else:
    print("Normal day")

# You can have multiple elif blocks
marks = 85

if marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Grade D")

###     some experiments with if, else, elif statements     ###

amount = 1500
if amount >= 1500:
    discounted_price = amount - 100
    print("Amount after discount:", discounted_price)
else:
    print("No discount applied. Total amount:", amount)