import sys
from EmployeeManager import employee_manager

def main_menu():
  app = employee_manager()
  while (True):  
    choice=input("Enter your choice: (Add : A, Delete: D, Show: S, Search/Check: C)").strip().upper()

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
      case _:
        print("Unknown Choice. Exiting...")
        sys.exit()

if __name__ == "__main__":
    main_menu()