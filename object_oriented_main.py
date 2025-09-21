from ResaleShope import  ResaleShop
from computer import Computer
import time

def main():

    # create computers for opening day
    mac1: Computer = Computer("mac1", "Mac OS", 800, 2024)
    pc1: Computer = Computer("pc1", "PC OS", 750, 2023)
    chrome1: Computer = Computer("chrome1","Chrome OS", 500, 2024)

    # set up shop
    shop: ResaleShop = ResaleShop([mac1, pc1, chrome1], 5000)
    print("")
    print("Welcome to your Computer Shop!")

    # game loop
    while True:
        print("")
        print("Would you like to buy, sell, or inspect any computers? Or view your current inventory or balance? Or close shop?")
        print("")
        time.sleep(1)
        print("Type: Buy, Sell, Inspect, Inventory, Balance, or Close")
        answer = input()

        # If user selects inventory 
        if answer == "Inventory":
            shop.getInventory()
            time.sleep(1)

        # If user selects balance
        if answer == "Balance":
            shop.getBalance()

        # If user wants to buy a computer:
        if answer == "Buy":

            # Ask what kind of computer they want
            print("")
            print("What is the name of the computer you would like to buy?")
            new_computer = input()
            print("")
            print("What is the year of the computer you would like to buy?")
            year = input()
            year = int(year)
            for idx in shop.inventory:
                if new_computer == idx.name:
                    print("")
                    print(f"You already have {new_computer}, please choose a different name:")
                    new_computer = input()
                else:
                    pass
            cost = 1000
            print("")

            # Ask if the cost is ok
            print(f"{new_computer} is ${cost}, would you like to buy it?")
            print("")
            print("Type: Yes or No")
            answer = input()

            # If buying a new computer:
            if answer == "Yes":
                # If user has the buyig power
                if shop.balance >= 1000:
                    shop.buy(new_computer, 1000, year)
                    print("Ok, your inventory and balance has been updated")
                    print()
                
                # If user doesnt have the buying power 
                if shop.balance < 1000:
                    print("")
                    print("You do not have sufficient funds")
                    print("")
            if answer == "No":
                print("Ok")
                print("")

        # if user wants to sell a computer
        if answer == "Sell":
            
            # Ask for Computer
            usercomp = shop.askForComp()

            # Sell computer
            shop.sell(usercomp)
            print("\nSold!")
            time.sleep(2)


        # if user wants to inspect a computer
        if answer == "Inspect":
            print("")
            print("Would you like to check the OS, price, or year of a computer? Would you like to refurbish a computer?")
            print("")
            print("Type: OS, Price, Year, or Refurbish")
            response = input()

            # get OS system
            if response == "OS":

                # get computer user is looking for
                usercomp = shop.askForComp()

                # if computer exist:
                if usercomp != False:
                    os = usercomp.getOS()
                    print(f"The OS is {os}")
                    print("")

                # Update OS, if user wants
                print("Would you like to Update OS?")
                print("")
                print("Type: Yes or No")
                answer = input()
                if answer == "Yes":
                    shop.updateOS(usercomp)
                    time.sleep(2)
                if answer == "No":
                    print("")
                    print("OS unchanged")
                    time.sleep(2)
                # if computer does not exist:

            # get price
            if response == "Price":

                # get computer user is looking for
                usercomp = shop.askForComp()

                # if computer exists:
                if usercomp != False:
                    price = usercomp.getPrice()
                    print(f"The price is {price}")
                    time.sleep(2)
                
                print(f"\nWould you like to update price? \n\nType Yes or No:")

                while True:
                    update_res = input()
                    if update_res == "Yes":
                        shop.updatePrice(usercomp)
                        break
                    if update_res == "No":
                        break
                    if update_res != "Yes" and update_res != "No":
                        print("Error: User did not enter Yes or No")
                        time.sleep(1)
                        print("\nType Yes or No:")
                        


            if response == "Year":

                # get computer user is looking for
                usercomp = shop.askForComp()

                if usercomp != False:
                    year = usercomp.getYear()
                    print(f"The year is {year}")
                    time.sleep(2)


            # refurbish
            if response == "Refurbish":
                print("\nWould you like to assign price based of year?")
                response = None
                while True:
                    print("\nType: Yes or No")
                    response = input()
                    if response != "Yes" or response != "No":
                        pass
                    if response == "No" or response == "Yes":
                        break
                if response == "Yes":
                    usercomp = shop.askForComp()
                    print("Refurishing ... ")
                    time.sleep(2)
                    shop.refurbish(usercomp)
                    print(f"\nPrice for {usercomp.name} is now ${usercomp.price}")
                    time.sleep(1)
                if response == "No":
                    print("\n Okay")
                    time.sleep(1)
                    pass
            # or type the wrong thing
        
        # closing shop, for good unfortunately
        if answer == "Close":
            time.sleep(1)
            print("\nOnce Shops closes, the Bank will own the property again.\nAre you sure you want to permanently close?")
            close = None
            # getting a yes or no
            while True:
                print("\nType: Yes or No")
                close = input()
                if close != "Yes" or close != "No":
                    pass
                if close == "No" or close == "Yes":
                    break
            # keeping shop open or closing
            if close == "Yes":
                break
            if close == "No":
                pass

if __name__ == "__main__":
    main()