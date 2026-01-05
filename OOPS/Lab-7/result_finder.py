class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self.__marks1 = 0
        self.__marks2 = 0
        self.__marks3 = 0

    def set_marks(self, marks1,marks2,marks3):
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3

    def get_marks(self):
        return self.__marks1, self.__marks2, self.__marks3
    

    
    """def set_marks1(self, marks):
        self.__marks1 = marks

    def set_marks2(self, marks):
        self.__marks2 = marks

    def set_marks3(self, marks):
        self.__marks3 = marks

    # --------- Get methods ---------
    def get_marks1(self):
        return self.__marks1

    def get_marks2(self):
        return self.__marks2

    def get_marks3(self):
        return self.__marks3
"""



    """
    Method to display marks obtained
    """
    def display_marks(self):
        print("Marks 1 :", self.__marks1)
        print("Marks 2 :", self.__marks2)
        print("Marks 3 :", self.__marks3)


    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        return self.__marks1 + self.__marks2 + self.__marks3

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        return self.get_total() / 3

    """
    Method to get the result for the marks given
    """
    def get_result(self):
        if (self.__marks1 >= 35 and self.__marks2 >= 35 and self.__marks3 >= 35):
            return "Pass"
        else:
            return "Fail"
