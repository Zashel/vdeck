"""Wise men say only fools rush in
But I can't help falling in love with you
Shall I stay? Would it be a sin?
If I can't help falling in love with you
Like a river flows surely to the sea
Darling so it goes some things are meant to be
Take my hand take my whole life too
For I can't help falling in love with you"""
                                                    #Elvis Presley
                                                    #And I'm a fool

import enum
import .vcardtypes

#------------ VDeck ------------#
class VDeck():
    """Main class for VDeck.
    It has a few nested classes"""       
    #------------ VDeck.VCard ------------#
    class VCard():
        """Class VCard to access properties individually"""
        #------------ VDeck.VCard.Status ------------#
        class Status(enum.Enum):
            """Status of VCards"""
            Deck = 0
            Hand = 1
            Table = 2
            Discarded = 3
            OffGame = 4
        
        #------------ VDeck.VCard.__init__ ------------#
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
            
        #------------ VDeck.VCard.__dir__ ------------#
        def __dir__(self):
            """Let's dir the properties too!"""
            return dir(self).update(self.properties)
            
        #------------ VDeck.VCard.__getattr__ ------------#
        def __getattr__(self, attr):
            """Let's get properties as attributes.
            As you can read in pydoc first of all it searches in __getattribute__ so..."""
            if attr in self.properties:
                return self.properties[attr]
            else:
                raise AttributeError
            
        #------------ VDeck.VCard @property ------------#
        @property
        def name(self):
            return self._name
        @property
        def status(self):
            return self._status
        @property
        def vdeck(self):
            return self._vdeck
        @property
        def visible(self):
            return self._visible
        @status.setter
        def status(self, status):
            assert(status, VDeck.VCard.Status)
            self.status = status
        @visible.setter
        def visible(self, visible):
            self._visible = visible and True or False #0 and None are False
            
        #------------ VDeck.VCard setters ------------#
        #This setter aren't setted as property to explicitly set them
        #They use the implicit setter
        #You may need both of them, they are not 'duplicated'
        def set_visible(self):
            """Set the card visible"""
            self.visible = True
        def set_hidden(self):
            """Set the card not visible"""
            self.visible = False
        def set_status(self, status):
            """Set the status of the card"""
            self.status = status
        def set_property(self, property_key, value):
            "Set a property of the card"""
            self._properties[property_key] = value
            
    def __init__(self, vdeck_type, cards=dict()):
        """Initialize the VDeck
        vdeck_type: a VDeck.Type enum
        cards: a dictionary setted by name: properties of each card"""
        assert isinstance(vdeck_type, vcardtypes.Types)
        self._type =vdeck_type
        if vdeck_type == vcardtypes.Types.Custom:
            assert cards is not dict()
        else:
            cards = vcardtypes.selector(vdeck_type)
        self._cards = [VDeck.VCard(name, cards[name]) for name in cards]
        
class Game():
    #TODO
    pass
    class Player():
        #TODO
        pass
    class Table():
        #TODO
        
