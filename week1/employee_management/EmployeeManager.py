class employee_manager:
    def __init__(self):
        self.next_employee_id = 4
        self.employees = {
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



    def add_employee(self):
        employee_name = input("Enter name of employee: ")
        employee_dept = input("Enter department of employee: ")
        employee_salary = input("Enter Salary of Employee: ")

        
        employee_details =  {"name" : employee_name , "department": employee_dept, "salary":employee_salary}
        self.employees[self.next_employee_id] = employee_details
        self.next_employee_id += 1
        print(f"Employee {employee_name} added succesfully")

    def search_employee(self):
        try :
            emp_id = int(input("Enter the ID which you want to search:").strip())
        except ValueError :
            print("Invalid input. Please enter a numerinc ID")

        if (emp_id in self.employees):
            print("Details of the requested employee are as follows:")
            print("----------------------------------------------------------------")
            print (f"EMPLOYEE ID : {emp_id}")
            print(f"\tName of Employee: {self.employees[emp_id]['name']}" )
            print(f"\tDepartment of Employee: {self.employees[emp_id]['department']}" )
            print(f"\tSalary of Employee: {self.employees[emp_id]['salary']}")
            print("----------------------------------------------------------------")
        else :
            print (f"Employee {emp_id} is not present")

    def delete_employee(self):
        try :
            emp_id = int(input("Enter the ID which you want to delete:").strip())
        except ValueError :
            print("Invalid input. Please enter a numeric ID.")
            return
    
        if emp_id in self.employees:
            print("Details of the requested employee are as follows:")
            print(f"\nName of Employee: {self.employees[emp_id]['name']}" )
            print(f"\nDepartment of Employee: {self.employees[emp_id]['department']}" )
            print(f"\nSalary of Employee: {self.employees[emp_id]['salary']}")
            confirmation = input("Are you sure to delete this employee? (Y: Yes) ").strip().upper()
            if ( confirmation == 'Y' ):
                del self.employees[emp_id]
                print(f"Removed employee {emp_id} so the updated list is : {self.show_employees()}")
            else :
                print("Not removed employee" )
        else :
            print(f"Unknown Employee: {emp_id} ")

    def show_employees(self):
        print("Details of the requested employee are as follows:")
        for ekey in self.employees.keys():
            print("----------------------------------------------------------------")
            print (f"EMPLOYEE ID : {ekey}")
            print(f"\tName of Employee: {self.employees[ekey]['name']}" )
            print(f"\tDepartment of Employee: {self.employees[ekey]['department']}" )
            print(f"\tSalary of Employee: {self.employees[ekey]['salary']}")
            print("----------------------------------------------------------------")




