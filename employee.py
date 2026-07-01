import sys
employees = ["Tushar","Mr X", "Hruday", "Amit", "Rushank"]

def add_employee():
    employee_name = input("Enter name of employee: ")
    employees.append(employee_name)
    print(f"Employee {employee_name} added succesfully")

def show_employees():
    print(f"Here is the list of employees: {employees}")


def search_employee():
    search_name = input("Enter the name of Employee: ").strip()
    if (search_name in employees):
       print(f"Following employee is present in list: {search_name}")
    else :
       print (f"Employee {search_name} is not present")

def delete_employee():
    emp_name = input("Enter the name which you want to delete:").strip()
    if (emp_name in employees):
        employees.remove(emp_name)
        print(f"Removed employee {emp_name} so the updated list is : {employees}")
    else :
       print(f"Unknown Employee: {emp_name} ")


def main_menu():
  while (True):  
    choice=input("Enter your choice: (Add : A, Delete: D, Show: S, Search/Check: C)").strip()

    match choice:
      case "A":
        add_employee()
        continue
      case "D":
        delete_employee()
        continue
      case "S":
        show_employees()
        continue
      case "C":
        search_employee()
        continue
      case _:
        print("Unknown Choice. Exiting...")
        sys.exit()

if __name__ == "__main__":
    main_menu()