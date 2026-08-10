from EmployeeClass import Employee

class EmployeeManager:
    def __init__(self):
        self.next_employee_id = 1
        self.employees = {}



    def add_employee(self):
        employee_name = input("Enter name of employee: ")
        employee_dept = input("Enter department of employee: ")
        try :
            employee_salary = int(input("Enter Salary of Employee: "))
        except ValueError :
            print ("Invalid Input. Please enter numeric salary")
            return


        new_emp = Employee(self.next_employee_id, employee_name , employee_dept,employee_salary)
        self.employees[self.next_employee_id] = new_emp
        self.next_employee_id += 1

        print(f"Employee {employee_name} added succesfully")

    def delete_employee(self):
        try :
            emp_id = int(input("Enter the ID which you want to delete:").strip())
        except ValueError :
            print("Invalid input. Please enter a numeric ID.")
            return
    
        empObj = self.get_employee(emp_id)
        if (empObj):
            empObj.display_employee_info()
            confirmation = input("Are you sure to delete this employee? (Y: Yes) ").strip().upper()
            if ( confirmation == 'Y' ):
                del self.employees[emp_id]
                print(f"Removed employee {emp_id} so the updated list is :")
                self.show_employees()
            else :
                print("Not removed employee" )
        else :
            print(f"Unknown Employee: {emp_id} ")
            return


    def search_employee(self):
        try :
            emp_id = int(input("Enter the ID which you want to search:").strip())
        except ValueError :
            print("Invalid input. Please enter a numerinc ID")
            return
        
        empObj = self.get_employee(emp_id)
        if (empObj):
            empObj.display_employee_info()
        else :
            print (f"Employee {emp_id} is not present")
            return


    def show_employees(self):
        print("Details of the all employee are as follows:\n")
        for empObj in self.employees.values():
            empObj.display_employee_info()

    def get_employee(self,emp_id):
        if (emp_id in self.employees):
            empObj=self.employees[emp_id]
            return empObj
        else :
            return None





