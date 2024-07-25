from cards import *

values = {
    "Zwei": 2, "Drei": 3, "Vier": 4, "Fünf": 5, "Sechs": 6, "Sieben": 7,
    "Acht": 8, "Neun": 9, "Zehn": 10, "Bube": 11, "Dame": 12, "König": 13, "Ass": 14
}

colors = ("♠️", "♣️", "♥️", "♦️")


class FrenchCard(Card):
    def __gt__(self, other: Card) -> bool:
        return self.value > other.value


class FrenchDeck(Deck):
    _cards = [FrenchCard(CardValue(k, values[k]), c) for k in values.keys() for c in colors]
    _name = "französisches Blatt"

    def __init__(self):
        super().__init__()
