from french_deck import FrenchDeck, FrenchCard
from cards import Hand


class PokerHand(Hand):
    def __init__(self):
        super().__init__()

    def __lt__(self, other: FrenchCard):
        pass
