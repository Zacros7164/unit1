class Shopkeeper(object):
    def __init__(self):
        self.items = [
            "small health potions",
            "medium health potions",
            "large health potions",
            "shield"
        ]
        self.prices = [
            5,
            8,
            10,
            15
        ]
        self.inventory = [
            15,
            10,
            5,
            1
        ]
    
    def initial_sales_pitch(self):
        print """
        I have %s for %i gold,
        %s for %i gold,
        %s for %i gold,
        and one %s, for %i gold.
        What would you like to see?"""

    def sales_pitch(self):
        print """
        I have %s for %i gold,
        %s for %i gold,
        and %s for %igold,
        What would you like to see?"""

    def purchase_request(self, hero_wallet, hero_inventory, player_selection):
        if hero_wallet < self.prices[player_selection]:
            print """
            I'm sorry you don't seem to have enough gold to buy that item,
            You should try fighting more monsters to gain more gold."""
        else: 
            print """
            Absolutely, and how many would you like?"""
            amounts = raw_input("> ")
            if amounts <= self.inventory[player_selection]:
                self.inventory[player_selection] -= amounts
                hero_inventory.append(player_selection)
                hero_inventory_amounts.append(player_selection)
            else: 