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
        # get its OS
    def getOS(self):
        return self.os
    
        #get its Price
    def getPrice(self):
        return self.price
    
        # get its year
    def getYear(self):
        return self.year

        # set its price
    def setPrice(self, price: int):
        self.price = price

        # set is operating system
    def setOS(self, operatingSystem: str):
        self.operatingSystem = operatingSystem