from collections import Counter

import pytest

from french_deck import *


class TestCards:

    def setup_method(self):
        self.cards = [Card(CardValue(k, v), "blank") for k, v in {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        }.items()]
        self.c1, self.c2, self.c3, self.c4, self.c5 = self.cards
        self.deck = Deck(self.cards, "Test-Deck")
        self.french_deck = FrenchDeck()
        self.h1 = Hand(max_hand=2)
        self.h2 = Hand(max_hand=2)
        self.h3 = Hand(max_hand=2)

    def test_card_value(self):
        assert self.c1.get_value() == 1
        assert self.c2.get_value() == 2

    def test_card_color(self):
        assert self.c1.get_color() == "blank"

    def test_draw_cards(self):
        self.h1.draw_cards(self.deck.deal(2, self.h1))
        assert len(self.h1) == 2
        assert len(self.deck) == 3
        self.h2.draw_cards(self.deck.deal(2, self.h2))
        assert len(self.h2) == 2
        assert len(self.deck) == 1

    def test_dont_deal_more_than_cards_in_deck(self):
        self.h1.draw_cards(self.deck.deal(2, self.h1))
        self.h2.draw_cards(self.deck.deal(2, self.h2))
        assert len(self.deck) == 1
        with pytest.raises(ValueError):
            self.h3.draw_cards(self.deck.deal(2, self.h3))
        assert len(self.h3) == 0
        assert len(self.deck) == 1

    def test_dont_deal_more_than_max_cards_for_hand_allowed(self):
        self.h1.draw_cards(self.deck.deal(2, self.h1))
        assert len(self.deck) == 3
        with pytest.raises(ValueError):
            self.h1.draw_cards(self.deck.deal(2, self.h1))
        # deck length keeps the same
        assert len(self.deck) == 3

    def test_french_deck(self):
        counted_values = Counter([c.get_value() for c in self.french_deck.list_cards()])
        counted_colors = Counter([c.get_color() for c in self.french_deck.list_cards()])
        assert len(self.french_deck) == 52                                # number of cards
        assert len(set(self.french_deck)) == len(list(self.french_deck))  # all cards unique
        assert sorted(counted_values.keys()) == list(range(2, 15))        # contains all values from 2 to 14
        assert all(value == 4 for value in counted_values.values())       # 4 suits/colors for every value
        assert all(value == 13 for value in counted_colors.values())      # 13 values for every color
