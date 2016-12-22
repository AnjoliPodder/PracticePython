'''
Solution by: Anjoli Podder
December 2016

http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/02_Control/Calculator/proj03.pdf

You calculator will perform addition, subtraction, multiplication and division. It will accept
floating-point values, and it will check for division by zero.
Input will be in the form:
operand operator operand
where operand can be any Real number and operator is +, -, *, or /.
The operator must be separated from the operands by at least one space, i.e. “4+3” will cause
Python to generate an error. We cannot protect ourselves from that error (yet) so we will
simply assume that the user will not make that error when entering values.
When you hit the Enter key, the result will be printed. If an illegal operand is used or division
by zero is attempted, an error message will be printed, but the program will continue asking for a
new expression to evaluate.
After a result is printed your program will ask if you wish to perform another calculation. If
‘y’ or ‘Y’ or ‘yes’ or ‘Yes’ or ‘YES’ is entered, another calculation can be performed, otherwise
the program will quit

'''

def calculator():
    validOperation = False
    while not(validOperation):
        operation = input("Please enter a mathematical operation in the form operand operator operand: ")
        try:
            entry = operation.split(" ")
            if len(entry) != 3:
                print("Sorry that was an invalid entry")
            else:
                operand1 = float(entry[0])
                operator = entry[1]
                operand2 = float(entry[2])
                if not(operator in "-+*/"):
                    print("Invalid input - operator must be +, -, / or *")
                else:
                    validOperation = True
        except:
            print("Sorry that was an invalid entry")
    if operator== "+":
        print(operand1 + operand2)
    elif operator == "-":
        print(operand1 - operand2)
    elif operator == "*":
        print(operand1 * operand2)
    elif operator == "/":
        if operand2 == 0:
            print("Invalid input - can't divide by zero")
        else:
            print(operand1 / operand2)
    again = input("Do you want to do another calculation? (Y/N) ")
    if again.lower() in ["y", "yes"]:
        calculator()
    else:
        print("Thanks for using the calculator!")

calculator()
