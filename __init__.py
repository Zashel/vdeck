"""Wise men say only fools rush in
But I can't help falling in love with you
Shall I stay? Would it be a sin?
If I can't help falling in love with you
Like a river flows surely to the sea
Darling so it goes some things are meant to be
Take my hand take my whole life too
For I can't help falling in love with you"""
                                                    #Frank Sinatra
import enum

class VDeck():
    """Main class for VDeck.
    It has a few nested classes"""
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
        
    class VCard():
        """Class VCard to access properties individually"""
        class Status(enum.Enum):
            """Status of VCards"""
            Deck = 0
            Hand = 1
            Table = 2
            Discarded = 3
            OffGame = 4
            
        def __init__(self, vdeck, name, properties=dict()):
            """Initialize a VCard:
            vdeck: wich VDeck is bound to
            name: name of card
            properties: a dictionary with custom properties of card"""
            self._name = name
            self._vdeck = vdeck
            self._status = VCard.Status.Deck
            self._visible = False
            self._properties = properties
            
        def __dir__(self):
            """Let's dir the properties too!"""
            return dir(self).update(self.properties)
            
        def __getattr__(self, attr):
            """Let's get properties as attributes.
            As you can read in pydoc first of all it searches in __getattribute__ so..."""
            if attr in self.properties:
                return self.properties[attr]
            else:
                raise AttributeError
            
    def __init__(self, cdeck_type, name_list=list(), properties_list=list()):
        assert isinstance(vdeck_type, VDeck.Types)
        
