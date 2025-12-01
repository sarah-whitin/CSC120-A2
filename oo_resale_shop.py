from Computer import Computer

class ResaleShop:
    inventory: list

    # Attributes:
        # inventory of all computers
    def __init__(self):
        self.inventory = []

    # buy = add to inventory
    def buy(self, new_computer: Computer):
        self.inventory.append(new_computer)

    # sell = remove from inventory
    def sell(self, sold:Computer):
        if self.inventory.contains(sold):
            self.inventory.remove(sold)
        else:
            print("Computer is not in inventory")
        

    # printing inventory for user
    def printInventory(self):
        print("")
        print("Your current computers include:")
        for idx in self.inventory:
            print(idx.name)
        # specifying if user has no computers
        if self.inventory == []:
            print("Shop has no computers.")

    # Refurbish
    def refurbish(self, comp : Computer):
        # assign price based off year
        if self.inventory.contains(comp):
            year = comp.getYear()
            if year < 2000:
                comp.setPrice(0)
            if year < 2012:
                comp.setPrice(250)
            if year < 2018:
                comp.setPrice(550)
            elif year >= 2018:
                comp.setPrice(1000)
        else:
            print("Computer is not in inventory")
