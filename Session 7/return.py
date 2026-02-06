def add(a, b):
    return a + b
def subtract(a, b):    
    return a - b
output = add(2, 3)  # This will return 5
subtract(output, 2)  # This will return 3
print(subtract(output, 2))  # This will print 3

def check_access(is_varified):
    if not is_varified:
        return "Access Denied"
    else:
        return "Access Granted"
print(check_access(False))  # This will print "Access Denied"
print(check_access(True))   # This will print "Access Granted"
        