def add_numbers(num1, num2):
    
    return num1 + num2,        

#example
def add_numbers(num1, num2):
    return num1 + num2, num1 * num2  # Returning the sum and the product of the two numbers

# Call the function
sum_result, product_result = add_numbers(4, 3)

print("Sum:", sum_result)         # Output: Sum: 7
print("Product:", product_result) # Output: Product: 12
