values = [3, 2, 1, 0, -1, -2, -3, 4]

## use break to exit the loop when a negative value is found

for val in values:
    if val < 0:
        print("Negative value found, stopping the loop.")
        break
    print("Current value:", val)

## use continue to skip negative values and print only non-negative values

for val in values:
    if val < 0:
        continue
    print("Current value:", val)