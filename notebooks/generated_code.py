Sure! Here is an example of a simple calculator function in Python that can perform basic arithmetic operations:

```python
def calculator(operator, num1, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        result = "Error: Invalid operator"
    
    return result

# Test the calculator function
print(calculator('+', 5, 3))  # Output: 8
print(calculator('-', 10, 2))  # Output: 8
print(calculator('*', 4, 5))  # Output: 20
print(calculator('/', 10, 2))  # Output: 5
print(calculator('/', 8, 0))  # Output: Error: Cannot divide by zero
print(calculator('%', 5, 3))  # Output: Error: Invalid operator
```

You can call the `calculator` function with an operator ('+', '-', '*', '/') and two numbers as arguments, and it will return the result of the arithmetic operation.