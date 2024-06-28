Sure! Here is an example of a simple calculator function in Python that can perform addition, subtraction, multiplication, and division:

```python
def calculator(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Invalid operation"

# Test the calculator function
print(calculator('add', 5, 3))  # Output: 8
print(calculator('subtract', 10, 4))  # Output: 6
print(calculator('multiply', 7, 2))  # Output: 14
print(calculator('divide', 20, 4))  # Output: 5
print(calculator('divide', 10, 0))  # Output: Error: Cannot divide by zero
print(calculator('power', 2, 3))  # Output: Invalid operation
```

You can call the `calculator` function with the operation you want to perform ('add', 'subtract', 'multiply', or 'divide') and the two numbers to operate on.