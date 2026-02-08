### Data ###
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}
### Complete functions ###

class SandwichMachine:
    # Initializes values inside of the sandwich machine class
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # Holding data for different ingredients to loop through
        items = ["bread", "ham", "cheese"]
        # looping a conditional to pull from recipes and check if the resources are sufficient enough
        # for the specified recipe
        for x in items:
            if self.machine_resources[x] < recipes[ingredients]["ingredients"][x]:
                print("Sorry there is not enough " + x)
                return False
                # Remove this else statement later as its just for testing
            else:
                print("Sufficient "+x)
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollar = float(input("How many dollars?: "))
        half = float(input("How many half dollars?: "))
        quarters = float(input("How many quarters?: "))
        nickels = float(input("How many nickels?: "))
        total = dollar*1.0 + half*0.5 + quarters*0.25 + nickels*0.05
        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            print("Here is $" + str(coins - cost) + " in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

### Make an instance of SandwichMachine class and write the rest of the codes ###
p1 = SandwichMachine(resources)
while True:
    print("What would you like? (small/ medium/ large/ off/ report)")
    size = input()
    # Taking input for resource size and then inserting into search function
    if size in ("small", "medium", "large"):
        if p1.check_resources(size):
            coins = p1.process_coins()
            p1.transaction_result(coins, recipes[size]["cost"])

    elif size == "off":
        quit()
    elif size == "report":
        print(p1.machine_resources)
        print(f"Size: {size}")
    else:
        print("Invalid input")