from computer import Computer
import time

class ResaleShop:
    inventory: list
    balance: float

    # Attributes:
        # inventory of all computers
    def __init__(self, startup:list, money:float):
        self.inventory = startup
        self.balance = money

    # price based on OS = refurbish

    def askForComp(self):
        while True:
            print("")
            print("Which computer?:")
            for idx in self.inventory:
                print(idx.name)
            print("")
            print("Type the name of the computer:")
            user_compname = input()
            usercomp = self.search(user_compname)
            if usercomp == False:
                time.sleep(1)
            if usercomp != False:
                return usercomp

    
    # look for computer the user asked for
    def search(self, compName: str):
        for idx in self.inventory:
            if compName == idx.name:
                return idx

        print("Computer does not exist")
        return False

    # buy = add to inventory
    def buy(self, bought:str, amt: float, year: int):
        new_computer: Computer = Computer(bought, f"{bought} OS", amt-100, year)
        self.inventory.append(new_computer)
        self.balance = self.balance-amt
            # sell = remove from inventory

    def sell(self, sold:Computer):
        self.inventory.remove(sold)

        # get amt from computer 
        amt = sold.price

        #update balance
        self.balance = self.balance+amt

    # printing inventory for user
    def getInventory(self):
        print("")
        print("Your current computers include:")
        for idx in self.inventory:
            print(idx.name)
        # specifying if user has no computers
        if self.inventory == []:
            print("Shop has no computers.")

    # tell user what balance is
    def getBalance(self):
        print("")
        print(f"Your current balance is: ${self.balance}")
    
    # update OS
    def updateOS(self, usercomp:Computer):
        print("")
        print("What is the new OS?")
        newOS = input()
        usercomp.os = newOS
        print("OS updated")

    # Update Price
    def updatePrice(self, usercomp: Computer):
        print("")
        print("What is the New Price?")
        print("")
        print("Type a Number:")
        input_price = input()
       # new_price = int(input_price)
        if input_price.isdigit() == True and int(input_price) >= 0:
            usercomp.price = int(input_price)
            print(f"\nNew Price of {usercomp.name} is ${usercomp.price}.")
            time.sleep(1)
        if input_price.isdigit() == False or int(input_price) < 0:
            print("Error: Requested price is not a positive integer")
            time.sleep(1)

    def refurbish(self, comp : Computer):
        # assign price based off year
        if comp.year < 2000:
            comp.price = 0
        if comp.year < 2012:
            comp.price = 250
        if comp.year < 2018:
            comp.price = 550
        elif comp.year >= 2018:
            comp.price = 1000
