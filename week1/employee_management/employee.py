import sys
from EmployeeManager import EmployeeManager
from EmployeeClass import Employee

def main_menu():
  app = EmployeeManager()
  while (True):  
    choice=input("Enter your choice: (Add : A, Delete: D, Show: S, Search/Check: C, Increment Salary: I)").strip().upper()

    match choice:
      case "A":
        app.add_employee()
        continue
      case "D":
        app.delete_employee()
        continue
      case "S":
        app.show_employees()
        continue
      case "C":
        app.search_employee()
        continue
      case "I":
        try :
          emp_id = int(input("Enter the employee ID of whose you want to increment the salary:").strip())
          percentage = int(input("Enter the percentage by which you want to increment the salary: ".strip()))
        except ValueError :
          print("Invalid input. Please enter a numeric ID")

        try : 
          employee = app.get_employee(emp_id)
          employee.increment_salary(percentage)
        except ValueError as e:
          print(e)
        except AttributeError as ae:
          print(f"Employee ID {emp_id} does not exists.")

      case _:
        print("Unknown Choice. Exiting...")
        sys.exit()

if __name__ == "__main__":
    main_menu()