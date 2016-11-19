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
    class Types(enum.Enum):
        French = 0
        Spanish = 1
        Spanish50 = 2
        Custom = 10
        
    class VCard():
        class Status(enum.Enum):
            Deck = 0
            Hand = 1
            Table = 2
            Discarded = 3
            OffGame = 4
            
        def __init__(self, vdeck, name, properties=dict()):
            self._name = name
            self._vdeck = vdeck
            self._status = VCard.Status.Deck
            self._visible = False
            self._properties = properties
            
        def __dir__(self):
            return dir(self).extend(self.properties)
            
        def __getattr__(self, attr):
            if attr in self.properties:
                return self.properties[attr]
            else:
                raise AttributeError
            
    def __init__(self, cdeck_type, name_list=list(), description_list=list()):
        assert isinstance(vdeck_type, VDeck.Types)
        
