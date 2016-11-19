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
    if vcard_type is Types.French:
        def french(suit, value, color):
            return {
                    "suit": suit,
                    "value": value,
                    "color": color
                    }
        suits = [
            "Spades",
            "Hearts",
            "Clovers",
            "Tiles"
            ]
        colors = [
            "Black",
            "Red"
            ]
        values = list(range(1, 11))
        values.extend(("J", "Q", "K"))
        for value in values:
            for ind_suit, suit in enumerate(suits):
                name = "{} of {}".format(value is not 1 and str(value) or "Ace", suit)
                deck[name] = french(suit, value, colors[ind_suit%2])
    return deck

