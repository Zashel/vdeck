"""Wise men say only fools rush in
But I can't help falling in love with you
Shall I stay? Would it be a sin?
If I can't help falling in love with you
Like a river flows surely to the sea
Darling so it goes some things are meant to be
Take my hand take my whole life too
For I can't help falling in love with you"""
                                                    #Elvis Presley

import enum
import random
import vcardtypes

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
            self._status = VDeck.VCard.Status.Deck
            self._visible = False
            self._properties = properties
            
        #------------ VDeck.VCard.__dir__ ------------#
        def __dir__(self):
            """Let's dir the properties too!"""
            return dir(self).update(self.properties)
            
        #------------ VDeck.VCard.__getattr__ ------------#
        def __getattr__(self, attr):
            """Let's get properties as attributes.
            As you can read in pydoc first of all it searches in 
            __getattribute__ so..."""
            if attr in self._properties:
                return self._properties[attr]
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
            assert isinstance(status, VDeck.VCard.Status)
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
            
    #------------ VDeck.__init__ ------------#
    def __init__(self, vdeck_type, cards=dict()):
        """Initialize the VDeck
        vdeck_type: a VDeck.Type enum
        cards: a dictionary setted by name: properties of each card"""
        #assert isinstance(vdeck_type, vcardtypes.Types) #¿?
        self._type =vdeck_type
        if vdeck_type == vcardtypes.Types.Custom:
            assert cards is not dict()
        else:
            cards = vcardtypes.selector(vdeck_type)
        self._cards = [VDeck.VCard(name, cards[name]) for name in cards]
        self._deck = self._cards.copy() #Anyway it would be referenced
        self._hands = list()
        self._discards = list()
        self._off_game = list()
        self._table = list()
        self._lists = (
                self._hands,
                self._table,
                self._deck,
                self._discards
                )
        
    #------------ VDeck @property ------------#
    @property
    def deck(self):
        return self._deck
    
    @property
    def discards(self):
        return self._discard
        
    @property
    def cards(self):
        return self._cards
        
    @property
    def hands(self):
        return self._hands
        
    @property
    def off_game(self):
        return self._off_game
        
    #------------ VDeck methods ------------#
    def _change_status(self, card, new_status, lists=None):
        if lists is None:
            lists = self._lists
        _status = VDeck.VCard.Status #This, children, is an alias
        assert isinstance(card, VDeck.VCard)
        assert isinstance(new_status, _status)
        status_dict = {
                _status.Deck: self._deck,
                _status.Hand: self._hands,
                _status.Discarded: self._discarded,
                _status.OffGame: self._off_game,
                _status.Table: self._table
                }
        for lst in lists:
            if card in lst:
                card.set_status(status)
                status_dict[status].append(card)
                lst.remove(card)
                break
                
    def destroy(self, card):
        """Destroy the card wherever it is"""
        #assert isinstance(card, VDeck.VCard) Not neccesary
        self._change_status(card, VDeck.VCard.Status.OffGame)
        
    def discard(self, card):
        """Discard the card wherever it is"""
        lists = (
                self._hands,
                self._table,
                self._deck
                )
        self._change_status(card, VDeck.VCard.Status.Discarded, lists)
                
    def draw(self):
        """Draw a card, it goes to hand"""
        card = self._deck.pop()
        card.set_status(VDeck.VCard.Status.Hand)
        self._hands.append(card)
        
    def play(self, card):
        """Play the card wherever it is"""
        lists = (
                self._hands,
                self._discarded,
                self._deck
                )
        self._change_status(card, VDeck.VCard.Status.Table, lists)
                
    def recover(self, card):
        """Draw a card from cementery. Discarded pile I mean."""
        if card in self._discarded:
            card.set_status(VDeck.VCard.Status.Hand)
            self._hand.append(card)
            self._discarded.remove(card)
        
    def shuffle_deck(self):
        """Suffle the deck, you fool!"""
        random.shuffle(self._deck) #I thought it would be harder. I love random
        
    def shuffle_discarded(self):
        """Shuffle the discarded pile"""
        random.shuffle(self._discarded)
        
    def _shuffle_x_on_deck(self, x):
        """Shuffle whatever on deck"""
        lists = (
                self._discarded,
                self._hands,
                self._table,
                self._off_game
                )
        is_card = False
        if isinstance(x, VDeck.VCard):
            x = [x]
        else:
            assert x in lists
        for card in x:
            card.set_status(VDeck.VCard.Status.Deck)
        self._deck.extend(x)
        if is_card is True:
            for lst in lists:
                if card in lst:
                    lst.remove(card)
                    break
        else:
            lists[lists.index(x)] = list() #Varible scopes. ;)
        self.shuffle_deck() #DO NOT REPEAT YOURSELF!
        
    def shuffle_discarded_on_deck(self):
        """Shuffle the discarded pile on deck"""
        self._shuffle_x_on_deck(self._discarded) #What did I say about repeting?
        
    def shuffle_hands_on_deck(self):
        """Shuffle the hands on deck"""
        self._shuffle_x_on_deck(self._discarded)
        
    def shuffle_table_on_deck(self):
        """Shuffle played on deck"""
        self._shuffle_x_on_deck(self._table)
        
    def shuffle_off_game_on_deck(self):
        """Shuffle off-game cards on deck"""
        self._shuffle_x_on_deck(self._off_game)
        
    def shuffle_card_on_deck(self, card): #In aras of readibility
        """Shuffle single card on deck"""
        self._shuffle_x_on_deck(self, card)
        
class Game():
    #TODO
    pass
    class Player():
        #TODO
        pass
    class Table():
        #TODO
        pass
