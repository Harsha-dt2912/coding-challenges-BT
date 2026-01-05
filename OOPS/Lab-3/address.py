class Address:
    def __init__(self):
        self.__address1=" "
        self.__address2=" "
        self.__city=" "
        self.__pincode=" "

    @property
    def address1(self):
        return self.__address1
    
    @address1.setter
    def address1(self,address1):
        self.__address1=address1

    @property
    def address2(self):
        return self.__address2
    
    @address2.setter
    def address2(self,address2):
        self.__address2=address2

    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self,city):
        self.__city=city

    @property
    def pincode(self):
        return self.__pincode
    
    @pincode.setter
    def pincode(self,pin):
        self.__pincode=pin

    