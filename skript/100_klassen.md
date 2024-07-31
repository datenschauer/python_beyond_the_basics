# Python und Objekte

Objekte spielen in Python eine grundlegende Rolle. So lautet schon der erste Satz über das sog. *Python Data Model* in der Python Dokumentation folgendermaßen:
> Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects.

Somit ist wirklich alles, mit was wir es in Python zu tun haben, ein Objekt. Egal, ob wir einen numerischen Typ definieren (`x = 3`) oder eine Liste (`x = [1, 2, 3]`). Immer definieren wir ein Objekt, das eine Identität (der Platz im Speicher), einen Typ (hier z.B. `int` oder `list`) und einen Wert (hier *3*, bzw. die Elemente *1, 2 und 3*) hat.
Diese Objekte sind die Bausteine unserer Programme, die wir mit Python schreiben.

Was ist aber, wenn wir unsere eigenen Objekte gestalten wollen (und wieso sollten wir das überhaupt wollen)?

## Objekte selbst gestalten

Beginnen wir bei unserem laufenden Beispiel, das ich in der Einleitung skizziert habe. Wir wollen ein Kartenspiel programmieren, genauer gesagt eine Poker-Variante, das man online gemeinsam und gegen einen KI-Gegner spielen kann.

Was sind die Grundbausteine eines Kartenspiels? Natürlich die Karten, oder? In unserem Programm können wir ohne diese Bausteine nicht auskommen. Jede Karte in einem "normalen" Kartenspiel (man denke an das französiche Blatt, das wir beim Poker brauchen) hat eine **Namen/Bezeichner** (z.B. "Ass"), einen **Wert** (z.B. 11 Punkte für den "Buben") und eine **Farbe** (z.B. Pik, Herz, etc.). Wir müssen diese Karten irgendwie modellieren. Wenn wir nun nicht wüssten, wie wir Objekte in Python bauen können, wie würden wir dann eine Karte, bzw. einen Stapel an Karten modellieren? Wahrscheinlich würden wir auf die einfachen Python Datenstrukturen, die wir kennen zurückgreifen. Vielleicht würden wir dazu ein Gemenge an Tupeln oder Dictionaries und Listen verwenden. Eine "Pokerhand" mit 5 Karten könnte dann so aussehen:

```python
poker_hand = [
    ("Ace", 14, "Heart"),
    ("King", 13, "Spades"),
    ("10", 10, "Diamond"),
    ("10", 10, "Spades"),
    ("4", 4, "Heart")
]
```

Wenn man nun den "Wert" dieser Hand berechnen will und dafür z.B. eine Funktion schreiben möchte, die prüft, ob ein Pärchen "vorhanden" ist, so könnte dies wiederum so aussehen:

```python
from collections import Counter

def has_pair(poker_hand):
    c = Counter([card[1] for card in poker_hand])
    return 2 in c.values()
    
has_pair(poker_hand)
```
> True

Ich möchte unsere Aufmerksamkeit vor allem auf die Zeile innerhalb der Funktion lenken, die die Werte zählt: `Counter([card[1] for card in poker_hand])`. Wenn wir diesen Code just in diesem Moment betrachten, dann ist uns klar, was `card[1]` bedeutet. Es liest den Wert der Karte aus dem Tupel aus. Aber ist uns das auch in vielen Wochen noch so klar? Wir könnten das Ganze immerhin mit einem Kommentar versehen. Man könnte auch auf die vielleicht noch bessere Idee kommen, für die Abbildung der Karten in unserem Modell eine Dictionary zu verweden; etwa so:

```
poker_hand = [
    {"name": "Ace", "value": 14, "color": "Heart"},
    {"name": "King", "value": 13, "color": "Spades"},
    ...
]
```

Und dementsprechend würde wir `Counter([card.get("value") for card in poker_hand])` aufrufen. Das ist sicherlich schon viel lesbarer. Doch was ist, wenn wir uns entscheiden, dass unser Karten-Objekt noch andere Werte braucht. Wie sieht eventuell mit Defaultwerten aus?
Datenstrukturen wie Tupel oder Dictionaries sind zwar sehr flexibel, aber wenn es darum geht mentale Objekte der echten Welt in ein programmatisches Modell zu überführen, dann macht es Sinn, die Möglichkeit zu haben, selbst Objekte anlegen zu können. Objekte, die ihre eigene "Identität" besitzen, und deren Einzigartigkeit aber auch Unterscheidbarkeit darin liegt, welche Attribute sie haben.

Doch es geht nicht nur um die Attribute von Objekten, sondern auch darum, was bestimmte Objekte **"tun"** können. Denken wir z.B. an das String-Objekt (`str`) in Python. Es kann mit Hilfe der `.upper()` Methode die einzelnene Zeichen ihrer Sequenz "groß schreiben". Könnte nicht so auch die "Pokerhand", die wir oben als normale Liste definiert haben, eine Methode haben? Was ist, wenn ein Nutzer aus seiner Pokerhand Karten abwirft, oder Karten aus seiner Hand einer anderen Hand gibt, oder die Karten in seiner Hand mischt. Wäre es da nicht gut, statt direkt mit Listen und anderen Datenstrukturen zu hantieren, einfach Methoden aufrufen zu können, wie:

```
poker_hand.throw(1)
poker_hand.deal(2, to=other_poker_hand)
poker_hand.shuffle()

poker_hand < other_poker_hand
```

Ja sogar einfach mit Vergleichsoperatoren die Wertigkeiten der einzelnen Hände, wie in der letzten Zeile zu vergleichen, wäre doch eine tolle Sache. Und genau das können Objekte in Python, Objekte, die wir uns selbst definieren können. Objekte, deren Benutzung unsere Code-Basis nicht nur sauber und aufgeräumt halten (welche Konzepte es hier genau gibt, sehen wir später noch), sondern auch den Code gerade bei komplexen Anwendungen lesbar halten. Und gerade die Lesbarkeit und Verständlichkeit von Code war immer schon eine der herausragenden Stärken von Python.

## Objekte und Klassen

Wie definieren wir also unsere eigenen Objekte in Python? Das erste, was wir dazu machen müssen, ist, uns eine **Klasse** zu definieren? Eine Klasse? Was ist das nun schon wieder für ein Konzept?
Kurz gesagt bilden Klassen die "Blaupause", bzw. den "Bauplan" für einen Typ von Objekten. Die Objekte werden so gebaut/gestaltet, wie es der Bauplan also die Klasse vorschreibt.
Am Beispiel des Karten-Objekts für unser Pokerspiel bedeutet dies, dass die Klasse folgendes als Bauplan definieren muss: jedes Kartenobjekt hat einen Namen, einen Wert und eine Farbe.

Man definiert eine Klasse mit dem Schlüsselwort `class`, gefolgt von einem Namen (die Konvention ist hier, dass Klassennamen immer groß geschrieben werden) und einem Doppelpunkt, der den eingerückten Block einleitet, in dem dann die Attribute und Methoden definiert werden.

```python
class Card:
    pass
```

Diese Klasse, obwohl wir noch keine Attribute oder Methoden definiert haben, können wir schon benutzen:

```python
c = Card()

c.name = "Ace"
c.value = 14
c.color = "♥️"

print(f"{c.name}, {c.value}, {c.color}")
```
> Ace, 14, ♥️

Python erlaubt es also, ein Objekt aus einer Klasse zu erzeugen und daran jegliches Attribut "anzuhängen", dass dann wieder aufgerufen werden kann. 
Doch möchte man seine Klassen schon ein bisschen "strikter" definieren. Wir wollen, dass eine Karte **immer** einen Namen, einen Wert und eine Farbe hat.

### Die __init__ Methode

Zu diesem Zweck gibt es eine spezielle Methode, die man in einer Klasse defnieren kann. Die sogenannte `__init__`-Methode.
Die Methode ist die erste und wichtigste der sog. **magic**, oder **special Methods** in Python, die wegen ihres doppelten Unterstrichs am Anfang und am Ende auch **dunder** (double under) **Methods** genannt werden. Wir werden einige weitere noch im Laufe dieses Kapitels kennen lernen.

Wenn wir nun diese `__init__` Methode implementieren lernen außerdem gleich etwas Generelles darüber, wie wir Methoden (auch ganz "normale") für eine Klasse in Python definieren.

Lassen Sie zunächst diesen Code auf sich wirken:

```python
class Card:

    def __init__(self, name, value, color):
        self.name = name
        self.value = value
        self.color = color

    def show_card(self):
        return f"{self.color} {self.name}"


c = Card("Ace", 14, "♥️")

c.show_card()
```
> ♥️  Ace

Hier sind nun einige Sachen zu erklären!
Die `__init__` Methode nimmt vier Parameter entgegen: `self, name, value` und `color`. Im "Body" dieser Funktion, werden dann die Attribute `name, value` und `color` dem Objekt `self`, das mit übergeben wurde zugeordnet. Dabei **müssen** die übergebenen Parameter und die damit definierten Attribute von `self` nicht den gleichen Namen haben. Es ist aber Konvention, und sicherlich auch nützlich für die Lesbarkeit des Codes, diese gleich zu benennen.

Wir sehen weiter, dass dann in der `show_card()` Methode im Body diese Attribute über das `self` Objekt wieder aufgerufen werden können.

Wir sehen letzens aber auch, dass bei der eigentlichen Erzeugung des Objekts beim Aufruf von `Card()` nur die Parameter `name`, `value` und `color`, nicht aber `self` übergeben werden müssen. Was hat das zu bedeuten?

Zunächst sollte man wissen, dass `self` nur eine Konvention ist. Es könnte auch `this` heißen, oder `dieses_objekt_hier`. Es ist aber **immer** und das gilt für **alle** Methoden einer Klasse, der **erste** Parameter in der Signatur einer Methode (selbst im Falle von `show_card()`, die ja ohne Parameter aufgerufen wird.

Die Implementierung von Klassen und Objekten in Python ist folgendermaßen implementiert:

