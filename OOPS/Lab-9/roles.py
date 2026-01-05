from enum import Enum


"""
    Fields of the class which are read only. Can't be assigned values again
"""

class Roles(Enum):
    DEVELOPER = 1
    TEST_ENGINEER = 2
    SR_DEVELOPER = 3
    DESIGNER = 4
