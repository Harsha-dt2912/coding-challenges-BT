class SalaryCalculator:
    """
    Method to calculate the salary of an employee
    """
    @staticmethod
    def get_salary(emp):
        salary = 0

    
        allowance = SalaryCalculator.get_allowance(emp)
        return emp.get_basic() + emp.get_hra() + allowance

    """
    Method to get the allowance for an employee based on the percentage
    """
    @staticmethod
    def get_allowance(emp):
        allowance = (emp.get_basic() * emp.get_allowance_percentage() / 100.0)
        return allowance
