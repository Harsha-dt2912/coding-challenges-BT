from salary_calculator import SalaryCalculator
from role_builder import RoleBuilder

class Employee:
    def __init__(self, emp_id=None, name=None, basic=0.0, hra=0.0, allowance_percentage=0.0, role=0):
        self.__emp_id = emp_id
        self.__name = name
        self.__basic = basic
        self.__hra = hra
        self.__allowance_percentage = allowance_percentage
        self.__role = role

    # setters 
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_basic(self, basic):
        self.__basic = basic

    def set_hra(self, hra):
        self.__hra = hra

    def set_allowance_percentage(self, allowance_percentage):
        self.__allowance_percentage = allowance_percentage

    def set_role(self, role):
        self.__role = role
    #getters

    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_basic(self):
        return self.__basic

    def get_hra(self):
        return self.__hra

    def get_allowance_percentage(self):
        return self.__allowance_percentage

    def get_role(self):
        return self.__role
    
    # business methods
    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)

    def get_salary(self):
        return SalaryCalculator.get_salary(self)

    def get_role_description(self):
        return RoleBuilder.get_role_description(self.__role)
