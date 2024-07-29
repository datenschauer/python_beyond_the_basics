import pytest
from french_deck import *
from poker_game import *


class TestPokerGame:
    """Tests derived from https://www.poker.org/poker-hands-ranking-chart/"""

    @pytest.fixture
    def deck(self):
        return FrenchDeck()

    @pytest.fixture
    def royal_flush(self):
        return PokerHand([
            FrenchCard(CardValue("Ass", 14), "♦️"),
            FrenchCard(CardValue("König", 13), "♦️"),
            FrenchCard(CardValue("Dame", 12), "♦️"),
            FrenchCard(CardValue("Bube", 11), "♦️"),
            FrenchCard(CardValue("Zehn", 10), "♦️"),
        ])

    @pytest.fixture
    def low_straight_flush(self):
        return PokerHand([
            FrenchCard(CardValue("2", 2), "♦️"),
            FrenchCard(CardValue("3", 3), "♦️"),
            FrenchCard(CardValue("4", 4), "♦️"),
            FrenchCard(CardValue("5", 5), "♦️"),
            FrenchCard(CardValue("6", 6), "♦️")
        ])

    @pytest.fixture
    def high_straight_flush(self):
        return PokerHand([
            FrenchCard(CardValue("2", 2), "♦️"),
            FrenchCard(CardValue("3", 3), "♦️"),
            FrenchCard(CardValue("4", 4), "♦️"),
            FrenchCard(CardValue("5", 5), "♦️"),
            FrenchCard(CardValue("6", 6), "♦️")
        ])

    @pytest.fixture
    def low_four_low_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("4", 4), "♠️"),
            FrenchCard(CardValue("4", 4), "♣️"),
            FrenchCard(CardValue("4", 4), "♥️"),
            FrenchCard(CardValue("4", 4), "♦️"),
            FrenchCard(CardValue("2", 2), "♠️")
        ])

    @pytest.fixture
    def low_four_high_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("4", 4), "♦️"),
            FrenchCard(CardValue("4", 4), "♣️"),
            FrenchCard(CardValue("4", 4), "♥️️"),
            FrenchCard(CardValue("4", 4), "♠️️"),
            FrenchCard(CardValue("5", 3), "♦️")
        ])

    @pytest.fixture
    def high_four(self):
        return PokerHand([
            FrenchCard(CardValue("K", 13), "♥️"),
            FrenchCard(CardValue("K", 13), "♦️"),
            FrenchCard(CardValue("K", 13), "♠️️"),
            FrenchCard(CardValue("K", 13), "♣️"),
            FrenchCard(CardValue("B", 11), "♣️")
        ])

    @pytest.fixture
    def full_house_high_3(self):
        return PokerHand([
            FrenchCard(CardValue("D", 12), "♣️"),
            FrenchCard(CardValue("D", 12), "♠️"),
            FrenchCard(CardValue("D", 12), "♥️"),
            FrenchCard(CardValue("9", 9), "♦️"),
            FrenchCard(CardValue("9", 9), "♥️")
        ])

    @pytest.fixture
    def full_house_low_3_high_2(self):
        return PokerHand([
            FrenchCard(CardValue("5", 5), "♠️"),
            FrenchCard(CardValue("5", 5), "♣️"),
            FrenchCard(CardValue("5", 5), "♥️"),
            FrenchCard(CardValue("K", 13), "♣️"),
            FrenchCard(CardValue("K", 13), "♦♠️")
        ])

    @pytest.fixture
    def full_house_low_3_low_2(self):
        return PokerHand([
            FrenchCard(CardValue("5", 5), "♦️"),
            FrenchCard(CardValue("5", 5), "♥️"),
            FrenchCard(CardValue("5", 5), "♣️"),
            FrenchCard(CardValue("10", 10), "♣️"),
            FrenchCard(CardValue("10", 10), "♦️")
        ])

    @pytest.fixture
    def high_flush(self):
        return PokerHand([
            FrenchCard(CardValue("D", 12), "♥️"),
            FrenchCard(CardValue("B", 11), "♥️"),
            FrenchCard(CardValue("9", 9), "♥️"),
            FrenchCard(CardValue("6", 6), "♥️"),
            FrenchCard(CardValue("3", 3), "♥️")
        ])

    @pytest.fixture
    def low_flush_high_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("B", 11), "♣️"),
            FrenchCard(CardValue("9", 9), "♣️"),
            FrenchCard(CardValue("6", 6), "♣️"),
            FrenchCard(CardValue("5", 5), "♣️"),
            FrenchCard(CardValue("3", 3), "♣️")
        ])

    @pytest.fixture
    def low_flush_low_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("B", 11), "♦️"),
            FrenchCard(CardValue("9", 9), "♦️"),
            FrenchCard(CardValue("6", 6), "♦️"),
            FrenchCard(CardValue("3", 5), "♦️"),
            FrenchCard(CardValue("2", 3), "♦️")
        ])

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

    @pytest.fixture
    def high_three(self):
        return PokerHand([
            FrenchCard(CardValue("A", 14), "♠️"),
            FrenchCard(CardValue("A", 14), "♣️"),
            FrenchCard(CardValue("A", 14), "♥️"),
            FrenchCard(CardValue("9", 9), "♥️"),
            FrenchCard(CardValue("6", 6), "♦️")
        ])

    @pytest.fixture
    def low_three_high_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("7", 7), "♠️"),
            FrenchCard(CardValue("7", 7), "♥️"),
            FrenchCard(CardValue("7", 7), "♣️"),
            FrenchCard(CardValue("B", 11), "♦️"),
            FrenchCard(CardValue("5", 5), "♥️")
        ])

    @pytest.fixture
    def low_three_low_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("7", 7), "♠️"),
            FrenchCard(CardValue("7", 7), "♥️"),
            FrenchCard(CardValue("7", 7), "♣️"),
            FrenchCard(CardValue("2", 2), "♦️"),
            FrenchCard(CardValue("5", 5), "♥️")
        ])

    @pytest.fixture
    def high_two_pair(self):
        return PokerHand([
            FrenchCard(CardValue("K", 13), "♠️"),
            FrenchCard(CardValue("K", 13), "♥️"),
            FrenchCard(CardValue("9", 9), "♣️"),
            FrenchCard(CardValue("9", 9), "♠️"),
            FrenchCard(CardValue("5", 5), "♦️")
        ])

    @pytest.fixture
    def low_two_pair_high_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("K", 13), "♣️"),
            FrenchCard(CardValue("K", 13), "♦️"),
            FrenchCard(CardValue("7", 7), "♥️"),
            FrenchCard(CardValue("7", 7), "♣️"),
            FrenchCard(CardValue("6", 6), "♦️")
        ])

    @pytest.fixture
    def low_two_pair_low_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("K", 13), "♣️"),
            FrenchCard(CardValue("K", 13), "♦️"),
            FrenchCard(CardValue("7", 7), "♥️"),
            FrenchCard(CardValue("7", 7), "♣️"),
            FrenchCard(CardValue("3", 3), "♦️")
        ])

    @pytest.fixture
    def high_pair(self):
        return PokerHand([
            FrenchCard(CardValue("K", 13), "♠️"),
            FrenchCard(CardValue("K", 13), "♥️"),
            FrenchCard(CardValue("9", 9), "♣️"),
            FrenchCard(CardValue("8", 8), "♣️"),
            FrenchCard(CardValue("7", 7), "♣️")
        ])

    @pytest.fixture
    def low_pair_high_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("9", 9), "♥️"),
            FrenchCard(CardValue("9", 9), "♣️"),
            FrenchCard(CardValue("8", 8), "♣️"),
            FrenchCard(CardValue("7", 7), "♣️"),
            FrenchCard(CardValue("6", 6), "♠️")
        ])

    @pytest.fixture
    def low_pair_low_kicker(self):
        return PokerHand([
            FrenchCard(CardValue("9", 9), "♥️"),
            FrenchCard(CardValue("9", 9), "♣️"),
            FrenchCard(CardValue("8", 8), "♣️"),
            FrenchCard(CardValue("5", 5), "♣️"),
            FrenchCard(CardValue("3", 3), "♠️")
        ])

    @pytest.fixture
    def highest_card_high(self):
        return PokerHand([
            FrenchCard(CardValue("B", 11), "♦️"),
            FrenchCard(CardValue("9", 9), "♣️"),
            FrenchCard(CardValue("7", 7), "♠️"),
            FrenchCard(CardValue("4", 4), "♦️"),
            FrenchCard(CardValue("3", 3), "♣️")
        ])

    @pytest.fixture
    def highest_card_low(self):
        return PokerHand([
            FrenchCard(CardValue("B", 11), "♥️"),
            FrenchCard(CardValue("7", 7), "♥️"),
            FrenchCard(CardValue("6", 6), "♠️"),
            FrenchCard(CardValue("3", 3), "♣️"),
            FrenchCard(CardValue("2", 2), "♥️")
        ])

    def test_ranking_hierarchy(self, royal_flush, high_straight_flush, low_straight_flush, low_four_low_kicker,
                               low_four_high_kicker, high_four, full_house_high_3, full_house_low_3_high_2,
                               full_house_low_3_low_2, high_flush, low_flush_high_kicker, low_flush_low_kicker,
                               high_straight, low_straight, high_three, low_three_high_kicker, low_three_low_kicker,
                               high_two_pair, low_two_pair_high_kicker, low_two_pair_low_kicker, high_pair,
                               low_pair_high_kicker, low_pair_low_kicker, highest_card_high, highest_card_low):
        assert (royal_flush > high_straight_flush > low_straight_flush > high_four > low_four_high_kicker
                > low_four_low_kicker > full_house_high_3 > full_house_low_3_high_2 > full_house_low_3_low_2
                > high_flush > low_flush_high_kicker > low_flush_low_kicker > high_straight > low_straight
                > high_three > low_three_high_kicker > low_three_low_kicker > high_two_pair > low_two_pair_high_kicker
                > low_two_pair_low_kicker > high_pair > low_pair_high_kicker > low_pair_low_kicker
                > highest_card_high > highest_card_low)

    def test_royal_flush(self, royal_flush):
        assert royal_flush.get_hand_rank().val == 10
        assert royal_flush.get_hand_rank().rank == PokerRank.RFlush

    def test_straight_flush(self, high_straight_flush, low_straight_flush):
        assert high_straight_flush.get_hand_rank().val == 9
        assert high_straight_flush.get_hand_rank().rank == PokerRank.SFlush
        assert high_straight_flush > low_straight_flush

    def test_four(self, high_four, low_four_high_kicker, low_four_low_kicker):
        assert high_four.get_hand_rank().val == 8
        assert high_four.get_hand_rank().rank == PokerRank.Four
        assert high_four > low_four_high_kicker > low_four_low_kicker

    def test_full_house(self, full_house_high_3, full_house_low_3_high_2, full_house_low_3_low_2):
        assert full_house_high_3.get_hand_rank().val == 7
        assert full_house_high_3.get_hand_rank().rank == PokerRank.FHouse
        assert full_house_high_3 > full_house_low_3_high_2 > full_house_low_3_low_2

    def test_flush(self, high_flush, low_flush_high_kicker, low_flush_low_kicker):
        assert high_flush.get_hand_rank().val == 6
        assert high_flush.get_hand_rank().rank == PokerRank.Flush
        assert high_flush > low_flush_high_kicker > low_flush_low_kicker

    def test_straight(self, low_straight, high_straight):
        assert low_straight.get_hand_rank().val == high_straight.get_hand_rank().val == 5
        assert low_straight.get_hand_rank().rank == high_straight.get_hand_rank().rank == PokerRank.Straight
        assert low_straight < high_straight

    def test_three(self, high_three, low_three_high_kicker, low_three_low_kicker):
        assert high_three.get_hand_rank().val == 4
        assert high_three.get_hand_rank().rank == PokerRank.Three
        assert high_three > low_three_high_kicker > low_three_low_kicker

    def test_two_pair(self, high_two_pair, low_two_pair_high_kicker, low_two_pair_low_kicker):
        assert high_two_pair.get_hand_rank().val == 3
        assert high_two_pair.get_hand_rank().rank == PokerRank.TwoPair
        assert high_two_pair > low_two_pair_high_kicker > low_two_pair_low_kicker

    def test_two(self, high_pair, low_pair_high_kicker, low_pair_low_kicker):
        assert high_pair.get_hand_rank().val == 2
        assert high_pair.get_hand_rank().rank == PokerRank.OnePair
        assert high_pair > low_pair_high_kicker > low_pair_low_kicker

    def test_highest(self, highest_card_high, highest_card_low):
        assert highest_card_high.get_hand_rank().val == 1
        assert highest_card_high.get_hand_rank().rank == PokerRank.Highest
        assert highest_card_high > highest_card_low
