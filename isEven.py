def is_even(number):
    
    return number % 2 == 0

# Example usage
num1 = 10
num2 = 7

# Checking if the numbers are even
result1 = is_even(num1)
result2 = is_even(num2)

print(f"Is {num1} even? {result1}")  # Output: Is 10 even? True
print(f"Is {num2} even? {result2}")  # Output: Is 7 even? False