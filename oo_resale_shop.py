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
        if sold in self.inventory:
            self.inventory.remove(sold)
        else:
            print("Computer is not in inventory")
        

    # printing inventory for user
    def printInventory(self):
        print("")
        print("Your current computers include:")
        for computer in self.inventory:
            print(computer.description)
        # specifying if user has no computers
        if self.inventory == []:
            print("Shop has no computers.")

    # Refurbish
    def refurbish(self, comp : Computer):
        # assign price based off year
        if comp in self.inventory:
            year = comp.yearMade
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

def main():
    shop = ResaleShop()
    comp1 = Computer("Used Mac", "M3", 2, 3, "Mac", 2020, 800)
    comp2 = Computer("oldie", "windows", 3, 2, "windows", 1990, 1000)
    shop.buy(comp1)
    shop.buy(comp2)
    shop.refurbish(comp1)
    shop.refurbish(comp2)
    shop.printInventory()
    print(comp1.price)
    print(comp2.price)

if __name__ == "__main__":
    main()
