import sys

employees = {
    1: {
        "name": "Tushar",
        "department": "Engineering",
        "salary": 4000000
    },
    2:{
        "name": "Rushank",
        "department": "Management",
        "salary": 6000000       
    },
    3:{
      "name": "Hruday",
      "department": "Creative",
      "salary": 8000000
    }

}

def add_employee():
    employee_name = input("Enter name of employee: ")
    employee_dept = input("Enter department of employee: ")
    employee_salary = input("Enter Salary of Employee: ")

    employee_id = max(employees) + 1

    employee_details =  {"name" : employee_name , "department": employee_dept, "salary":employee_salary}

    employees[employee_id] = employee_details
    #employees.append(employee_name)
    print(f"Employee {employee_name} added succesfully")

def show_employees():
    for id,detail in employees.items():
      print (f"ID : {id}")

      for key,value in detail.items():
         print(f"\t {key} : {value}")



def search_employee():
    try :
      emp_id = int(input("Enter the ID which you want to search:").strip())
    except ValueError :
      print("Invalid input. Please enter a numerinc ID")

    if (emp_id in employees):
        print("Details of the requested employee are as follows:")
        print(f"\nName of Employee: {employees[emp_id]['name']}" )
        print(f"\nDepartment of Employee: {employees[emp_id]['department']}" )
        print(f"\nSalary of Employee: {employees[emp_id]['salary']}")
    else :
       print (f"Employee {emp_id} is not present")

def delete_employee():
    try :
       emp_id = int(input("Enter the ID which you want to delete:").strip())
    except ValueError :
       print("Invalid input. Please enter a numeric ID.")
       return
    
    if emp_id in employees:
        print("Details of the requested employee are as follows:")
        print(f"\nName of Employee: {employees[emp_id]['name']}" )
        print(f"\nDepartment of Employee: {employees[emp_id]['department']}" )
        print(f"\nSalary of Employee: {employees[emp_id]['salary']}")
        confirmation = input("Are you sure to delete this employee? (Y: Yes) ").strip().upper()
        if ( confirmation == 'Y' ):
          del employees[emp_id]
          print(f"Removed employee {emp_id} so the updated list is : {employees}")
        else :
           print("Not removed employee" )
    else :
       print(f"Unknown Employee: {emp_id} ")


def main_menu():
  while (True):  
    choice=input("Enter your choice: (Add : A, Delete: D, Show: S, Search/Check: C)").strip().upper()

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