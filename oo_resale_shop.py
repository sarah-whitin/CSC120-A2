from ResaleShope import  ResaleShop

def main():
    # getting original inventory
    myShop: ResaleShop = ResaleShop(["mac1", "pc1", "chrome1", "mac2", "hp1", "mac3", "hp2015"])
    print("og inventory:", end="" )
    myShop.getInventory()

    # buying a computer 
    myShop.buy("mac2025")
    print("updated inventory:", end="" )
    myShop.getInventory()

    # selling a computer
    myShop.sell("pc1")
    print("updated inventory:", end="" )
    myShop.getInventory()


if __name__ == "__main__":
    main()