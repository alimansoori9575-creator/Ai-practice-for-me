def multiple_values(a):
    sum = 0
    for i in range(a):
        sum = sum + i
        avg = sum / a
    return sum, avg
s, av = multiple_values(5)
print(s) 
print(av)

def stats(values):
    return len(values), sum(values)

result = stats([1, 2, 3])
print(result)  # This will print (3, 6) because there are 3 values and their sum is 6

