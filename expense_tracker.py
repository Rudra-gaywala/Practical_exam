import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


class ExpenseTracker:

    def __init__(self):
        self.data = None

    def Load_dataset(self):
        path = input("\nEnter your file path : ")

        try :
            self.data = pd.read_csv(path)
            print("\nFile loaded successfully..............")
        except Exception as e :
            print(f"Error : {e}")


    def add_expenses(self) :
        if self.data is not None :
            date = input("Enter the date of expense (in : YYYY-MM-DD) : ")
            amount = float(input("Enter the expense amount (must be positive and in float): "))
            category = input("Enter the category of expense : ")
            description = input("Enter the description of expense : ")

            file = open("expenses.csv" , "w" )
            file.write([date,amount,category,description])
            file.close()

            print("\nExpense entry added successfully ...........")


        else :
            print("\nPlease load dataset first............")



class main :

    et = ExpenseTracker()
    
    while True:
        print("===============================================")

        print("\nSmart Expense Tracker Application.")

        print("\n=============================================")

        print("\n1. Load Dataset")
        print("2. Enter new entries")
        print("3. Show Dataset")
        print("4. Filter dataset")
        print("5. Show dataset summary")
        print("6. Data visualization")
        print("7. Exit")

        choice = int(input("\nEnter your choice : "))

    

        match choice :

            case 1:
                et.Load_dataset()

            case 2:
                et.add_expenses()

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 6:
                pass

            case 7:
                print("Exiting the program......Thank you............")
                break

            case _:
                print("Invalid choice...... please try again..............")

main()