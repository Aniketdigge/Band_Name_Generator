from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+":add, 
    "-":subtract, 
    "*":multiply, 
    "/":divide
}

def calculator():
    print(logo)
    choise = "y"
    num1 = float(input("What's the first number?: "))

    for symbol in operation:
        print(symbol)

    while choise == "y":
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        opertion_function = operation[operation_symbol]
        answer = opertion_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choise = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if choise == "y":
            num1=answer
        else:
            choise="n"
            calculator()

calculator()
    




