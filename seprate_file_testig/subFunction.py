
def Print_function(userl):   
    if "say" in userl:
        print(userl[4:], "\n")

def Clear_function(userl):
    if "cls" in userl[0:4]:
        Line_Number = 0
        os.system("cls")
        print("""
                                            Welcome to the Simple language
                                            Developed by Dhiraj Gholap
                                            DM Dhiraj For Source code
                                            Instagram id - dhiraj._._._
    """)
def add_numbers():
    while True:
        total = 0

        try:
            num_to_add = int(input("Enter the number to add: "))
            if num_to_add <= 0:
                print("Please enter a positive number.")
                return

            for i in range(num_to_add):
                user_input = input(f"Enter number {i+1}: ")
                try:
                    number = int(user_input)
                    total += number
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    return

            print(f"The sum of the entered numbers is: {total}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

def user_input():
    pass

