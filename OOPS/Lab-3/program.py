from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        emp.empid=int(input("Enter Employee Id: "))
        emp.empname=input("Enter Employee Name: ")
        emp.gender=input("Enter Gender: ")
        

        addr = emp.address
        addr.address1=input("Enter Address 1: ")
        addr.address2=input("Enter Address 2: ")
        addr.city=input("Enter City: ")
        addr.pincode=input("Enter Pincode: ")


    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        # print("Employee Id : ")
        # print("Employee Name : ")
        # print("Employee Gender : ")

        # print("Employee Address : --------------")
        # print("Address 1 : ")
        # print("Address 2 : ")
        # print("City : ")
        # print("PinCode : ")
        # print("----------------------------------")
    
        print("\n----- Employee Details -----")
        print("Employee Id :", emp.empid)
        print("Employee Name :", emp.empname)
        print("Employee Gender :", emp.gender)
        addr = emp.address
        print("\nEmployee Address :")
        print("Address 1 :", addr.address1)
        print("Address 2 :", addr.address2)
        print("City :", addr.city)
        print("Pincode :", addr.pincode)
        print("----------------------------")

if __name__ == "__main__":
    Program.main([])
