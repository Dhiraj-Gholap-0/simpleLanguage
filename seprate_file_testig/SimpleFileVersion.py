# main.py

import os
import subFunction as tools
from tkinter import messagebox

def main():
    os.system("cls")
    Variable_Dictionary = {}
    Line_Number = 0

    try:
        with open("Demo.simple", "r") as file:
            code_lines = file.readlines()

        for line_number, user in enumerate(code_lines, start=1):
            user = user.strip().lower()

            tools.variable_assign(user, Variable_Dictionary)
            tools.say_value_of_variable(user, Variable_Dictionary)
            tools.store_variable_value(user, Variable_Dictionary)
            tools.print_variable_value(user, Variable_Dictionary)

            if "cls" in user[0:3]:
                os.system("cls")

            if "say" in user:
                if user[4].isdigit() or user[4] == '-':
                    result = tools.calculate_expression(user[4:], Variable_Dictionary)
                    print(result)
                else:
                    print(user[4:])

            if user == "system fad denge":
                break

    except IndexError:
        messagebox.askyesno("Extra Space", "Remove the extra space after the code like new line etc.")

if __name__ == "__main__":
    main()
