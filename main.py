"""
Next: save and reopen decks.
"""

class DeckBox:
    def __init__(self, **kwargs):
        self.decks = kwargs.get('decks', [])


class Deck:
    def __init__(self, name, commander, **kwargs):
        self.name = name
        self.commander = commander
        self.groups = kwargs.get('groups', [Group("Nonlands", []), Group("Lands", [])])       # List of groups

    def add_card(self, card, group_name):
        for group in self.groups:
            if group.name == group_name:
                group.cards.append(card)
                break
            else:
                raise Exception("There is no such group in deck")


class Group:
    def __init__(self, name, cards):
        self.name = name       
        self.cards = cards      # List of Cards


class Card:
    def __init__(self, name, **kwargs):
        self.name = name
        self.qty = kwargs.get('qty', 1)


class Menu:
    items = []

    def print_menu(self):
        statement = "----------  Menu  ----------\n\n"
        for item in self.items:
            statement += " - {}\n".format(item)
        statement += "\n----------------------------"
        print(statement)




# Test items

test_deck = Deck("Orvar Wizards", Card("Orvar, the All-form"))

main_menu = Menu()
main_menu.items.append("Make new deck")
main_menu.print_menu()