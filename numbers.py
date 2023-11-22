result = None
operator = None
operand = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            user_input = input("Enter number: ")
            operand = float(user_input)
            if operator and operator == "+":
                result += operand
            elif operator and operator == "-":
                result -= operand
            elif operator and operator == "*":
                result *= operand
            elif operator and operator == "/":
                result /= operand
            else:
                result = operand

            wait_for_number = False
        else:
            user_input = input("Enter operator: ")
            if user_input == "=":
                print(result)
                break
            if user_input == '+' or user_input == '-' or user_input == '/' or user_input == '*':
                operator = user_input
                wait_for_number = True
            else:
                print("Not a valid operator. Try again.")

    except ValueError:
        print(f'{user_input} not valid input')
