"""
Class to represent employee information
"""
from address import Address
class Employee:
    def __init__(self):
        self.__empid=""
        self.__empname=""
        self.__gender=""
        self.__address=Address()

    @property
    def empid(self):
        return self.__empid
    
    @empid.setter
    def empid(self,id):
        self.__empid=id

    @property
    def empname(self):
        return self.__empname
    
    @empname.setter
    def empname(self,name):
        self.__empname=name

    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self,gender):
        self.__gender=gender
        
    @property
    def address(self):
        return self.__address
    
  