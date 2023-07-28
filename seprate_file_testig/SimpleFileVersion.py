import os
import subFunction as tools


# List_Of_Keywords = {"number input add":0,"variable name is":0,"say":0,"cls":0,"if ":0,"tell value of ":0,"and value is":0}

def variable_assign(line, variables):
    if 'variable name is ' in line:
        variable_info = line.split("variable name is ")[1].split(" and value is ")
        variable_name = variable_info[0].strip()
        variable_value = variable_info[1].strip()

        # Check if the input value is an integer
        if variable_value.isdigit():
            variables[variable_name] = int(variable_value)
        # Check if the input value is a float
        elif "." in variable_value and all(char.isdigit() or char == "." for char in variable_value):
            variables[variable_name] = float(variable_value)
        else:
            # If the value is not a number, store it as a string
            variables[variable_name] = variable_value

def say_value_of_variable(line, variables):
    if "tell value of " in line:
        variable_name = line.split("tell value of ")[1].strip()

        if variable_name in variables:
            print(f"The value of the variable {variable_name} is {variables[variable_name]}")
            # print(type(variables[variable_name]))
        else:
            print(f"The variable {variable_name} is not defined.")

def main():
    os.system("cls")
    print("""
        Welcome to the Simple language
        Developed by Dhiraj Gholap
        DM Dhiraj For Source code
        Instagram id - dhiraj._._._
    """)

    Variable_Dictionary = {}
    Line_Number = 0

    # Read the code from "demo.simple" file
    with open("Demo.simple", "r") as file:
        code_lines = file.readlines()

    for user in code_lines:
        Line_Number += 1
        user = user.strip().lower()

        if user == "system fad denge":
            break

        if "say" in user:
            print(user[4:], "\n")

        if "cls" in user[0:4]:
            Line_Number = 0
            os.system("cls")
            print("""
                Welcome to the Simple language
                Developed by Dhiraj Gholap
                DM Dhiraj For Source code
                Instagram id - dhiraj._._._
            """)

        variable_assign(user, Variable_Dictionary)
        say_value_of_variable(user, Variable_Dictionary)

    if "number input add" in user:
            operands = user.split("number input add ")[1].split("+")
            result = 0

            for operand in operands:
                operand = operand.strip()
                if operand.isdigit():
                    result += int(operand)
                elif operand in Variable_Dictionary:
                    result += Variable_Dictionary[operand]
                else:
                    print(f"Invalid operand: {operand} is not a valid number or variable.")
                    break
            else:
                print(f"The result of the addition is: {result}")

    if user[:3] == "if ":
        nextline = input("....")
        tools.Print_function(nextline)
    
    

if __name__ == "__main__":
    main()
