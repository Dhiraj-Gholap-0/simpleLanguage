# subFunction.py

import os

def Print_function(userl):   
    if "say" in userl:
        print(userl[4:], "\n")

def Clear_function(userl):
    if "cls" in userl[0:4]:
        os.system("cls")
        print("""
Welcome to the Simple language
Developed by Dhiraj Gholap
DM Dhiraj For Source code
Instagram id - dhiraj._._._
        """)

def variable_assign(line, variables):
    if 'variable name is ' in line:
        variable_info = line.split("variable name is ")[1].split(" and value is ")
        variable_name = variable_info[0].strip()
        variable_value = variable_info[1].strip()

        if variable_value.isdigit():
            variables[variable_name] = int(variable_value)
        elif "." in variable_value and all(char.isdigit() or char == "." for char in variable_value):
            variables[variable_name] = float(variable_value)
        else:
            variables[variable_name] = variable_value

def say_value_of_variable(line, variables):
    if "tell value of " in line:
        variable_name = line.split("tell value of ")[1].strip()

        if variable_name in variables:
            print(f"The value of the variable {variable_name} is {variables[variable_name]}")
        else:
            print(f"The variable {variable_name} is not defined.")

def calculate_expression(expression, variables):
    try:
        # Replace variable references with their values in the expression
        for variable_name in variables:
            expression = expression.replace(variable_name, str(variables[variable_name]))

        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def store_variable_value(line, variables):
    if "var " in line and "=" in line:
        variable_info = line.split("var ")[1].split("=")
        variable_name = variable_info[0].strip()
        variable_value = variable_info[1].strip()

        if variable_value.isdigit():
            variables[variable_name] = int(variable_value)
        elif "." in variable_value and all(char.isdigit() or char == "." for char in variable_value):
            variables[variable_name] = float(variable_value)
        else:
            variables[variable_name] = variable_value


def print_variable_value(line, variables):
    if "tell " in line:
        variable_name = line.split("tell ")[1].strip()

        if variable_name in variables:
            print(variables[variable_name])
        else:
            print(f"The variable {variable_name} is not defined.")
