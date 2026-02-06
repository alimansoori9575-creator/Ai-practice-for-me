def get_name():
    name = input("Enter your name: ")
    return name

def make_upper(name):
    return name.upper()
def main():
    name = get_name()
    upper_name = make_upper(name)
    print(f"Your name in uppercase is: {upper_name}")

main()