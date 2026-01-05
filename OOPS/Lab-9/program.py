from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = [None] * 2

        """
        emp = None

        emp_id = ""
        name = ""
        report_date = ""
        allowance_percentage = 0.0
        basic = 0.0
        hra = 0.0
        role = 0
        """

        # Accept employee information from the user
        print("Enter employee information")

        for i in range(len(employees)):
            print("Employee No : " + str(i+1))
            emp = Employee()   # empty object 

            emp.set_emp_id(input("Id : "))
            emp.set_name(input("Name : "))
            emp.set_basic(float(input("Basic : ")))
            emp.set_hra(float(input("HRA : ")))
            emp.set_allowance_percentage(float(input("Allowance Percentage : ")))

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER.value) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER.value))
            print(str(Roles.TEST_ENGINEER.value) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER.value))
            print(str(Roles.SR_DEVELOPER.value) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER.value))
            print(str(Roles.DESIGNER.value) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER.value))
            emp.set_role(int(input("Enter Role Id : ")))

            employees[i] = emp

            # Note: Original C# code does not assign Employee object to Employees array

        report_date = input("\nEnter report date (dd/mm/yyyy) : ")

        report = EmployeeReport(report_date)
        report.display_employees(employees)


        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
