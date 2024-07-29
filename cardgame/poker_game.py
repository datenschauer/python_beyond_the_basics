from collections import Counter
from dataclasses import dataclass
from french_deck import FrenchCard
from enum import Enum

from cards import Hand


class PokerRank(Enum):
    RFlush = "Royal Flush"
    SFlush = "Straight Flush"
    Four = "Four of a Kind"
    FHouse = "Full House"
    Flush = "Flush"
    Straight = "Straight"
    Three = "Three of a Kind"
    TwoPair = "Two Pairs"
    OnePair = "One Pair"
    Highest = "High Card"


@dataclass(frozen=True)
class PokerHandResult:
    val: int
    rank: PokerRank
    addendum: dict[str, list | Counter] | list


def all_equal_or_lower(l1: list[int], l2: list[int]) -> bool:
    for i, _ in enumerate(l1):
        if l1[i] < l2[i]:
            return True
    return False


def first_or_highest_kicker_is_lower(first_result: PokerHandResult, second_result: PokerHandResult) -> bool:
    s1st, *sRest = first_result.addendum["counts"]
    o1st, *oRest = second_result.addendum["counts"]
    if s1st == o1st:
        return all_equal_or_lower(sRest, oRest)
    return s1st < o1st


def first_or_second_lower(first_result: PokerHandResult, second_result: PokerHandResult) -> bool:
    first1st, first2nd = first_result.addendum["counts"]
    second1st, second2nd = second_result.addendum["counts"]
    if first1st == second1st:
        return first2nd < second2nd
    return first1st < second1st


class PokerHand(Hand):
    _MAX_HAND = 5

    def __init__(self, cards: list[FrenchCard]) -> None:
        super().__init__(max_hand=self._MAX_HAND, cards=cards)

    def _list_values(self) -> list[int]:
        return [card.get_value() for card in self._cards]

    def _count_values(self) -> Counter:
        return Counter([card.get_value() for card in self._cards])

    def _count_colors(self) -> Counter:
        return Counter([card.get_color() for card in self._cards])

    def _is_straight(self) -> bool:
        min_val = min(self._list_values())
        possible_straight_cards = range(min_val, min_val + self._MAX_HAND)
        return set(self._list_values()) == set(possible_straight_cards)

    def _is_flush(self) -> bool:
        return any([count == self._MAX_HAND for count in self._count_colors().values()])

    def get_hand_rank(self) -> PokerHandResult:
        values = sorted([c.get_value() for c in self._cards], reverse=True)
        value_counts = self._count_values().values()
        is_straight = self._is_straight()
        is_flush = self._is_flush()

        if is_straight and is_flush and max(self._list_values()) == 14:
            return PokerHandResult(10, PokerRank.RFlush, values)

        if is_straight and is_flush:
            return PokerHandResult(9, PokerRank.SFlush, values)

        if 4 in value_counts:
            return PokerHandResult(8, PokerRank.Four, {"counts": self._count_values()})

        if 3 in value_counts and 2 in value_counts:
            return PokerHandResult(7, PokerRank.FHouse, {"counts": self._count_values()})

        if is_flush:
            return PokerHandResult(6, PokerRank.Flush, values)

        if is_straight:
            return PokerHandResult(5, PokerRank.Straight, values)

        if 3 in value_counts:
            return PokerHandResult(4, PokerRank.Three, {"counts": self._count_values()})

        if list(value_counts).count(2) == 2:
            return PokerHandResult(3, PokerRank.TwoPair, {"counts": self._count_values()})

        if 2 in value_counts:
            return PokerHandResult(2, PokerRank.OnePair, {"counts": self._count_values()})

        return PokerHandResult(1, PokerRank.Highest, values)

    def __eq__(self, other):
        if not isinstance(other, PokerHand):
            raise TypeError(f"Cannot compare {type(self)} to {type(other)}")

        return (self.get_hand_rank().val == other.get_hand_rank().val
                and self.get_hand_rank().addendum == other.get_hand_rank().addendum)

    def __lt__(self, other):
        if not isinstance(other, PokerHand):
            raise TypeError(f"Cannot compare {type(self)} to {type(other)}")
        selfRank, otherRank = self.get_hand_rank(), other.get_hand_rank()

        # ties are not allowed in Poker
        # if there are the same ranks, other conditions matter
        if selfRank.val == otherRank.val:
            match selfRank:
                case PokerHandResult(_, PokerRank.Highest, addendum):
                    # the next highest card wins!
                    return all_equal_or_lower(addendum, otherRank.addendum)

                case PokerHandResult(_, PokerRank.OnePair, _):
                    # highest pair wins, if the same, kicker wins!
                    return first_or_highest_kicker_is_lower(selfRank, otherRank)

                case PokerHandResult(_, PokerRank.TwoPair, addendum):
                    # highest or next highest pair wins, else: kicker wins!
                    s1stPair, s2ndPair, *sRest = sorted(addendum["counts"], reverse=True)
                    o1stPair, o2ndPair, *oRest = sorted(otherRank.addendum["counts"], reverse=True)
                    if s1stPair == o1stPair and s2ndPair == o2ndPair:
                        return all_equal_or_lower(sRest, oRest)
                    elif s1stPair == o1stPair:
                        return s2ndPair < o2ndPair
                    return s1stPair < o1stPair

                case PokerHandResult(_, PokerRank.Three, _):
                    # highest three wins, else highest kicker wins!
                    return first_or_highest_kicker_is_lower(selfRank, otherRank)

                case PokerHandResult(_, PokerRank.Straight, addendum):
                    return max(addendum) < max(otherRank.addendum)

                case PokerHandResult(_, PokerRank.Flush, addendum):
                    return all_equal_or_lower(addendum, otherRank.addendum)

                case PokerHandResult(_, PokerRank.FHouse, _):
                    return first_or_second_lower(selfRank, otherRank)

                case PokerHandResult(_, PokerRank.Four, _):
                    return first_or_second_lower(selfRank, otherRank)

                case PokerHandResult(_, PokerRank.SFlush, addendum):
                    return max(addendum) < max(otherRank.addendum)

        return selfRank.val < otherRank.val

    def __gt__(self, other):
        return not self.__lt__(other)
