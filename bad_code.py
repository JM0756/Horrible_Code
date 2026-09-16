def thing(a, b, c):
    x = a
    y = b
    if c == "yes":
        z = 0
        z = x
        z = z + y
        return z
    else:
        return a + b


def stuff(a, b):
    x = 0
    x = a
    x = x + b
    print("The answer is:", x)


def calculate(a, b, operation):
    if operation == "add":
        result = 0
        result = a
        result = result + b
        print("The answer is:", result)

    elif operation == "subtract":
        result = 0
        result = a
        result = result - b
        print("The answer is:", result)

    elif operation == "multiply":
        result = 0
        result = a
        result = result * b
        print("The answer is:", result)

    elif operation == "divide":
        if b == 0:
            print("You can't divide by zero!")
        else:
            result = 0
            result = a
            result = result / b
            print("The answer is:", result)

    else:
        print("I don't know what you want me to do.")

    if operation == "add":
        print("You selected addition.")
    if operation == "subtract":
        print("You selected subtraction.")
    if operation == "multiply":
        print("You selected multiplication.")
    if operation == "divide":
        print("You selected division.")


def main():
    print("Welcome to the amazing calculator")
    
    first = input("Enter first number: ")
    second = input("Enter second number: ")

    first = float(first)
    second = float(second)

    print("Type add, subtract, multiply, or divide")
    what = input("What do you want to do? ")

    calculate(first, second, what)

    if what == "add":
        x = first
        x = x + second
        print("Just to make sure, the answer is:", x)

    if what == "subtract":
        x = first
        x = x - second
        print("Just to make sure, the answer is:", x)


main()