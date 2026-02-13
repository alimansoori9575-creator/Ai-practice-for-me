# "r" when use this it will allow you to read only 
file = open(r"C:\Users\91917\Desktop\Sessions\Ai-practice-for-me\Session 9\hello.txt", "r")
print(file.read())
file.close()

# Using with statement -----> with this we don't need to use close
with open(r"C:\Users\91917\Desktop\Sessions\Ai-practice-for-me\Session 9\hello.txt", "r") as fly:
     print(fly.read())


# if we want to read line by line
with  open(r"C:\Users\91917\Desktop\Sessions\Ai-practice-for-me\Session 9\hello.txt", "r") as file:
    for line in file:
        col = line.strip()
        if col == "Ali Mansoori":
         continue
        print(col)

# store all lines in a list

with  open(r"C:\Users\91917\Desktop\Sessions\Ai-practice-for-me\Session 9\hello.txt", "r") as file:
    line = file.readline()
    print(line)