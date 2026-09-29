def ones(num):
    return num % 10

def tens(num):
    return (num // 10) % 10

def hundreds(num):
    return (num // 100) % 10

def thousands(num):
    return (num // 1000) % 10

def sum_digits(num):
    return ones(num) + tens(num) + hundreds(num) + thousands(num)

num = int(input("Enter a number (0 to 9999): "))

print(f"Ones place is {ones(num)}.")
print(f"Tens place is {tens(num)}.")
print(f"Hundreds place is {hundreds(num)}.")
print(f"Thousands place is {thousands(num)}.")
print(f"Sum of all digits is {sum_digits(num)}.")