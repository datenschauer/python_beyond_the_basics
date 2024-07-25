import random


class CardValue:
    name: str
    value: int

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, CardValue):
            return False
        if self.name == other.name and self.value == other.value:
            return True
        return False

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return self.name


class Card:
    value: CardValue
    color: str

    def __init__(self, value: CardValue, color: str):
        self.value = value
        self.color = color

    def beats(self, other) -> bool:
        pass

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        if self.value == other.value and self.color == other.color:
            return True
        return False

    def __repr__(self):
        return f"({self.color} {self.value})"

    def __str__(self):
        return f"({self.color} {self.value})"


class Deck:
    _cards: list[Card]
    _name: str

    def __init__(self):
        self._shuffle()
        self._current_cards = [card for card in self._cards]

    def _shuffle(self) -> None:
        random.shuffle(self._cards)

    def list_cards(self) -> list[Card]:
        return self._current_cards

    def deal(self, num_of_cards: int) -> list[Card]:
        if num_of_cards > len(self._current_cards):
            raise ValueError(f"Not enough cards to deal! Only {len(self._current_cards)} left.")
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
        return f"{self._name}: {len(self)}"


class Hand:
    _cards: list[Card]

    def __init__(self):
        self._cards = []

    def add_cards(self, cards: list[Card]) -> None:
        for card in cards:
            self._cards.append(card)

    def play_card(self, index: int) -> Card:
        return self._cards.pop(index)

    def show_cards(self) -> list[Card]:
        return self._cards

    def __len__(self) -> int:
        return len(self._cards)

    def __contains__(self, card: Card) -> bool:
        return card in self._cards

    def __iter__(self):
        return iter(self._cards)
