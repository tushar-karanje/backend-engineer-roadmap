class Employee:
    def __init__(self, employee_id: int, employee_name: str, employee_dept: str, employee_salary: int):
        self.id = employee_id
        self.name = employee_name
        self.dept = employee_dept
        self.salary = employee_salary

    
    def display_employee_info(self):
        print(f"Details of the employee with ID: {self.id} is as follows:")
        print("----------------------------------------------------------------")
        print(f"\tName of Employee: {self.name}" )
        print(f"\tDepartment of Employee: {self.dept}" )
        print(f"\tSalary of Employee: {self.salary}")
        print("----------------------------------------------------------------")

    def increment_salary(self,percentage):
        if (percentage <= 0 ) :
            raise ValueError("Increment percentage must be greater than zero.")
        incremented_salary = (self.salary * percentage)/100
        self.salary += incremented_salary

