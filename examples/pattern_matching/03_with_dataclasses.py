from dataclasses import dataclass


@dataclass
class Book:
    author: str
    title: str
    publisher: str


@dataclass
class VideoGame:
    title: str
    publisher: str
    platform: str


def print_values(obj: Book | VideoGame):
    match obj:
        case Book(author, title, _):
            print(f"The Book '{title}' was written by {author}.")
        case VideoGame(title, publisher, platform):
            print(f"The Game '{title}' was produced by {publisher} for {platform}.")


if __name__ == '__main__':
    b1 = Book("Luciano Ramalho", "Fluent Python", "O'Reilly")
    b2 = Book("Harry J.W. Percival & Bob Gregory", "Architectural Patterns with Python", "O'Reilly")
    v1 = VideoGame("Super Mario Bros", "Nintendo", "NES")
    v2 = VideoGame("Final Fantasy VII", "Square-Enix", "Playstation")

    objects = [b1, b2, v1, v2]

    for obj in objects:
        print_values(obj)
