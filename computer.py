class Computer:
    description: str
    processorType: str
    hardDriveCapacity: int
    memory: int
    operatingSystem: str
    yearMade: int
    price: int

    # Setting up attributes:
        # OS
        # Price 
    def __init__(self,description: str, processorType: str, hardDriveCapacity: int, memory: int, operatingSystem: str, yearMade: int, price: int):
        self.description = description
        self.processorType = processorType
        self.hardDriveCapacity = hardDriveCapacity
        self.memory = memory
        self.operatingSystem = operatingSystem
        self.yearMade = yearMade
        self.price = price

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

        # set its price
    def setPrice(self, price: int):
        self.price = price

    def setOS(self, operatingSystem: str):
        self.operatingSystem = operatingSystem