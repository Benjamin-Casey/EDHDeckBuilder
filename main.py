"""
Next: Save and reopen decks.
"""
import pickle

class DeckPickler(pickle.Pickler):
    pass


class DeckUnpickler(pickle.Unpickler):
    pass


class DeckBox:
    """Stores deck objects for the user

    Attributes:
        name : str
            The name of the deck box
        decks : list[Deck], optional
            Stores the decks that are contained within the deckbox (default
            is empty)
    """
    def __init__(self, name, decks = []):
        self.name = name
        self.decks = decks


class Deck:
    """Stores information regarding cards and commander for the deck

    Attributes:
        name : str
            Name of the deck
        commander : Card
            The decks desginated commander. 
            Note: this currently only allows for one commander.
            TODO change this
        groups : list[Group], optional
            Stores the groups that are used within the deck (defualt is Lands,
            Nonlands)

    Methods:
        add_card(card, group_name)
            Adds the given card to the given group
    """
    def __init__(self, name, commander, groups=[Group("Nonlands"), Group("Lands")]):
        self.name = name
        self.commander = commander
        self.groups = groups

    def add_card(self, card, group_name):
        for group in self.groups:
            if group.name == group_name:
                group.cards.append(card)
                break
            else:
                raise Exception("There is no such group in deck")


class Group:
    """Stores cards of a particular category for a deck

    Attributes:
        name : str
            Name of the group/category
        cards : list[Card], optional
            Stores cards in the group (default is empty)
    """
    def __init__(self, name, cards=[]):
        self.name = name       
        self.cards = cards      # List of Cards


class Card:
    """Holds MTG card information

    Attributes:
        name : str
            Name of the card
        qty : int, optional
            Amount of that card in the group (default is 1)
    """
    def __init__(self, name, qty=1):
        self.name = name
        self.qty = qty


class Menu:
    """Displays information in a list for hte menu of the main loop

    Attributes:
        items : list
            List of optional actions that the user can input to use the app

    Methods:
        print_menu()
            Prints the menu and its contents (items)
    """
    items = []

    def print_menu(self):
        statement = "----------  Menu  ----------\n\n"
        for item in self.items:
            statement += " - {}\n".format(item)
        statement += "\n----------------------------"
        print(statement)


"""Test items"""

# test_deck = Deck("Orvar Wizards", Card("Orvar, the All-form"))

# main_menu = Menu()
# main_menu.items.append("Make new deck")
# main_menu.print_menu()