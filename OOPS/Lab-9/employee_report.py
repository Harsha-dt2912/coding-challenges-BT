class EmployeeReport:

    def __init__(self, report_date):
        self.report_date = report_date

    def print_line(self):
        print("---------------------------------------------------------------------------")

    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT")
        print("Date :", self.report_date)
        self.print_line()
        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        self.print_line()

    def display_footer(self, count):
        self.print_line()
        print("Total Employees :", count)
        self.print_line()

    def display_employees(self, employees):
        self.display_header()

        for emp in employees:
            print(
                f"{emp.get_emp_id()}\t{emp.get_name()}\t{emp.get_role_description()}\t"
                f"{emp.get_basic()}\t{emp.get_hra()}\t{emp.get_allowance()}\t{emp.get_salary()}"
            )

        self.display_footer(len(employees))
