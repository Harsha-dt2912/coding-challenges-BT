from result_finder import ResultFinder

class Program:
    @staticmethod
    def main(args):
        # Accept the values from command line arguments
        marks1 = int(args[0])
        marks2 = int(args[1])
        marks3 = int(args[2])

        # Store the values entered in the object
        finder = ResultFinder()
        finder.set_marks(marks1, marks2, marks3)
        
        """ 
        finder.set_marks1(marks1)
        finder.set_marks2(marks2)
        finder.set_marks3(marks3)
        """

        # Display all the information with the help of get and other methods
       
        print("\nMarks entered-------------")
        finder.display_marks()
        """
        print("Marks 1 :",finder.get_marks1())
        print("Marks 2 :",finder.get_marks2())
        print("Marks 3 :",finder.get_marks3())
        """
        print("Total :", finder.get_total())
        print("Average :", finder.get_average())
        print("Result :", finder.get_result())

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
