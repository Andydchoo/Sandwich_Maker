class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # Prompting user to insert their coin denominations one by one
        # then calculating their total and returning it
        dollars = ""
        half = ""
        quarters = ""
        nickels = ""
        print("Please insert coins.")

        # Error check if the user doesnt input a integer
        while dollars.isdigit() == False:
            dollars = input("How many dollars?: ")
            if dollars.isdigit() == False:
                print("Error. Not an integer.")
        while half.isdigit() == False:
            half = input("How many half dollars?: ")
            if half.isdigit() == False:
                print("Error. Not an integer.")
        while quarters.isdigit() == False:
            quarters = input("How many quarters?: ")
            if quarters.isdigit() == False:
                print("Error. Not an integer.")
        while nickels.isdigit() == False:
            nickels = input("How many nickels?: ")
            if nickels.isdigit() == False:
                print("Error. Not an integer.")
        dollars = float(dollars)
        half = float(half)
        quarters = float(quarters)
        nickels = float(nickels)
        total = dollars * 1.0 + half * 0.50 + quarters * 0.25 + nickels * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        # Conditional for if the user put in enough money then give their change back
        # then return true. Otherwise tell them not enough and refund.
        if coins >= cost:
            print("Here is $" + str(round((coins - cost), 2)) + " in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False