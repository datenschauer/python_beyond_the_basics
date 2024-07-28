import pytest
from french_deck import *
from poker_game import *


class TestPokerGame:
    """Tests derived from https://www.poker.org/poker-hands-ranking-chart/"""

    @pytest.fixture
    def deck(self):
        return FrenchDeck()

    @pytest.fixture
    def low_straight(self):
        return PokerHand([
            FrenchCard(CardValue("2", 2), "♣️"),
            FrenchCard(CardValue("3", 3), "♥️"),
            FrenchCard(CardValue("4", 4), "♠️"),
            FrenchCard(CardValue("5", 5), "♥️"),
            FrenchCard(CardValue("6", 6), "♣️")
        ])

    @pytest.fixture
    def high_straight(self):
        return PokerHand([
            FrenchCard(CardValue("6", 6), "♥️"),
            FrenchCard(CardValue("7", 7), "♥️"),
            FrenchCard(CardValue("8", 8), "♦️"),
            FrenchCard(CardValue("9", 9), "♦️"),
            FrenchCard(CardValue("10", 10), "♦️")
        ])

    def test_straight(self, low_straight, high_straight):
        assert low_straight.get_hand_rank().val == high_straight.get_hand_rank().val == 5
        assert low_straight.get_hand_rank().rank == high_straight.get_hand_rank().rank == PokerRank.Straight
        assert low_straight < high_straight

