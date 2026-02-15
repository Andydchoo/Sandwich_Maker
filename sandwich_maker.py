
items = ["bread", "ham", "cheese"]
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # looping a conditional to pull from recipes and check if the resources are sufficient enough
        # for the specified recipe
        for x in items:
            if self.machine_resources[x] < ingredients[x]:
                print("Sorry there is not enough " + x)
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        # Looping through the inventory and subtracting the ingredients used from
        # the specified recipe
        for x in items:
            self.machine_resources[x] -= order_ingredients[x]