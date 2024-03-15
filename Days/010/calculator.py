import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(art.logo)
    num1 = float(input("What is the first number? "))
    for operand in operations:
        print(operand)

    again = True

    while again is True:
        operation_symbol = input("Pick an operation. ")
        num2 = float(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (
            input(
                "Do you want to make a calculation with the answer? Y for yes and N for no: "
            )
            == "Y"
        ):
            num1 = answer
        else:
            again = False
            calculator()


calculator()
