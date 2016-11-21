import enum

class Types(enum.Enum):
	"""Preset deck types:
	French Deck
	Original 40 cards Spanish deck
	50 Cards Spanish deck
	Custom deck
	"""
	#TODO: Tarot Deck

	French = 0
	Spanish = 1
	Spanish50 = 2
	Custom = 10

def selector(vcard_type):
    """Returns a dictionary with name and properties of chosen preset deck"""
    #French Deck
    deck = dict()   
    french_suits = [
            "Spades",
            "Hearts",
            "Clovers",
            "Tiles"
            ]
    spanish_suits = [
            "Oros",
            "Copas",
            "Espadas",
            "Bastos"
            ]
    colors = [
            "Black",
            "Red"
            ]
    def spanish_deck(values):
        deck = dict()
        for value in values:
            for ind_suit, suit in enumerate(spanish_suits):
                name = str(value)
                if value == 10:
                    name = "Sota"
                elif value == 11:
                    name = "Caballo"
                elif value == 3:
                    name = "Rey"
                mus = value
                if value == 2:
                    mus = 1
                elif value == 3:
                    mus = 10
                elif value > 10:
                    mus = 10
                name = "{} de {}".format(name, suit)
                deck[name] = dict(suit=suit, value=value, mus=mus)
        return deck
    if vcard_type is Types.French:
        values = list(range(1, 11))
        values.extend(("J", "Q", "K"))
        for value in values:
            for ind_suit, suit in enumerate(french_suits):
                name = "{} of {}".format(value is not 1 and str(value) or "Ace", suit)
                deck[name] = dict(suit=suit, value=value, color=colors[ind_suit%2])
    elif vcard_type is Types.Spanish:
        values = list(range(1,8))
        values.extend(range(10,13))
        deck = spanish_deck(values)
    elif vcard_type is Types.Spanish50:
        values = list(range(1,13))
        deck = spanish_deck(values)
                
    return deck

