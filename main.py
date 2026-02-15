import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        print("What would you like? (small/ medium/ large/ off/ report)")
        size = input()
        # Taking input for resource size and then inserting into search function
        if size in ("small", "medium", "large"):
            # Checking if order can be made
            if sandwich_maker_instance.check_resources(recipes[size]["ingredients"]):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, recipes[size]["cost"]):
                    sandwich_maker_instance.make_sandwich(size, recipes[size]["ingredients"])
                    print(size + " sandwich is ready. Bon appetit!")
        elif size == "off":
            quit()
        elif size == "report":
            # Looping through the different items in inventory and printing
            # for x in items:
            #     print(f"{x}: {sandwich_maker_instance.machine_resources[x]}")
            #  If the slices and pounds is necessary then here is the included code commented out
            print("Bread: " + str(sandwich_maker_instance.machine_resources["bread"]) + " slice(s)")
            print("Ham: " + str(sandwich_maker_instance.machine_resources["ham"]) + " slice(s)")
            print("Cheese: " + str(sandwich_maker_instance.machine_resources["cheese"]) + " ounce(s)")
        else:
            print("Invalid input")

if __name__=="__main__":
    main()
