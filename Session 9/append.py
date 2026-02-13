with open('output.txt', 'a') as file:
    file.write('And Zaid you too')

# now using log
name = input('Enter your Name:')
with open('output.log', 'a') as file:
    file.write('Program started.\n')
    file.write(f'Hello {name}!\n')
    file.write('Program ended.\n')