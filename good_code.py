class calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

my_calculator = calculator()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

match operation:
   case "add":
       result = my_calculator.add(num1, num2)
   case "subtract":
       result = my_calculator.subtract(num1, num2)
   case "multiply":
       result = my_calculator.multiply(num1, num2)
   case "divide":
       result = my_calculator.divide(num1, num2)
   case _:
       print("Invalid operation.")
print(f"The result is: {result}")


