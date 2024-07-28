import random


class CardValue:
    _name: str
    _value: int

    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value

    def get_value(self):
        return self._value

    def show_name(self):
        return self._name

    def __eq__(self, other):
        if not isinstance(other, CardValue):
            return False
        if self._name == other.show_name() and self._value == other.get_value():
            return True
        return False

    def __lt__(self, other):
        return self._value < other.get_value()

    def __gt__(self, other):
        return self._value > other.get_value()

    def __str__(self):
        return self._name


class Card:
    _card_value: CardValue
    _color: str

    def __init__(self, value: CardValue, color: str):
        self._card_value = value
        self._color = color

    def beats(self, other) -> bool:
        pass

    def get_value(self):
        return self._card_value.get_value()

    def get_color(self):
        return self._color

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        if self._card_value == other.get_value() and self._color == other.get_color():
            return True
        return False

    def __repr__(self):
        return f"({self._color} {self._card_value.show_name()})"

    def __str__(self):
        return f"({self._color} {self._card_value.show_name()})"

    def __hash__(self):
        return hash(self._card_value.show_name() + self._color)


class Hand:
    _cards: list[Card]
    _MAX_HAND: int

    def __init__(self, max_hand: int = None, cards: list[Card] = None):
        if max_hand:
            self._MAX_HAND = max_hand
        if cards:
            self._cards = cards
        else:
            self._cards = []

    def draw_cards(self, cards: list[Card]) -> None:
        if self._cards == self._MAX_HAND:
            raise ValueError(f"Can't add any more cards! Max number of cards in hand reached!")
        if len(self._cards) + len(cards) > self._MAX_HAND:
            raise ValueError(f"Can't add that much cards! Only {self._MAX_HAND - len(self._cards)} left to hold.")
        for card in cards:
            self._cards.append(card)

    def throw_away(self):
        self._cards = []

    def play_card(self, index: int) -> Card:
        return self._cards.pop(index)

    def show_cards(self) -> list[Card]:
        return self._cards

    def max_hand(self) -> int:
        return self._MAX_HAND

    def __repr__(self):
        return f"{[f'{i}: {c}' for i, c in enumerate(self._cards)]}"

    def __len__(self) -> int:
        return len(self._cards)

    def __contains__(self, card: Card) -> bool:
        return card in self._cards

    def __iter__(self):
        return iter(self._cards)


class Deck:
    _cards: list[Card]
    _name: str

    def __init__(self, cards=None, name=None):
        if cards:
            self._cards = cards
        if name:
            self._name = name
        self._shuffle()
        self._current_cards = [card for card in self._cards]

    def _shuffle(self) -> None:
        random.shuffle(self._cards)

    def list_cards(self) -> list[Card]:
        return self._current_cards

    def deal(self, num_of_cards: int, to: Hand) -> list[Card]:
        if num_of_cards > len(self._current_cards):
            raise ValueError(f"Not enough cards to deal! Only {len(self._current_cards)} left.")
        if maxy := to.max_hand() - len(to) < num_of_cards:
            raise ValueError(f"Can't deal so many cards! Hand can only hold {maxy}")
        cards = []
        for _ in range(num_of_cards):
            cards.append(self._current_cards.pop())
        return cards

    def reset(self) -> None:
        self._shuffle()
        self._current_cards = [card for card in self._cards]

    def __len__(self) -> int:
        return len(self._current_cards)

    def __contains__(self, card: Card) -> bool:
        return card in self._current_cards

    def __iter__(self):
        return iter(self._current_cards)

    def __next__(self):
        return self._current_cards.pop()

    def __repr__(self):
        return f"{self._name}: {len(self._current_cards)}"
