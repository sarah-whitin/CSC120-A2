class Computer:
    name: str
    os: str
    price: float
    year: int

    # Setting up attributes:
        # OS
        # Price 
    def __init__(self, name: str, system:str, value: float, year: int):
        self.name = name
        self.os = system
        self.price = value
        self.year = year

    # Methods: 
    # Things the computer can do for itself
        # Know its OS
    def getOS(self):
        return self.os
    
        #Know its Price
    def getPrice(self):
        return self.price
    
        # KNow its year
    def getYear(self):
        return self.year