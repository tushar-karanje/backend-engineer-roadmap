employees = []

def add_employee():
    employee_name = input("Enter name of employee: ")
    employees.append(employee_name)
    print(f"Employee {employee_name} added succesfully")

def show_employees():
    employees.append(["Tushar","Mr X", "Hruday", "Amit", "Rushank"])
    print(f"Here is the list of employees: {employees}")


def search_employee():
    pass

def delete_employee():
    pass

def main_menu():
  while (True):  
    choice=input("Enter your choice: (Add, Delete, Show, Search)").strip()

    match choice:
      case "Add":
        add_employee()
        break
      case "Delete":
        delete_employee()
        break
      case "Show":
        show_employees()
        break
      case "Search":
        search_employee()
        break
    

if __name__ == "__main__":
    main_menu()