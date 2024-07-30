# Python und Objekte

Objekte spielen in Python eine grundlegende Rolle. So lautet schon der erste Satz über das sog. *Python Data Model* in der Python Dokumentation folgendermaßen:
> Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects.

Somit ist wirklich alles, mit was wir es in Python zu tun haben, ein Objekt. Egal, ob wir einen numerischen Typ definieren (`x = 3`) oder eine Liste (`x = [1, 2, 3]`). Immer definieren wir ein Objekt, das eine Identität (der Platz im Speicher), einen Typ (hier z.B. `int` oder `list`) und einen Wert (hier *3*, bzw. die Elemente *1, 2 und 3*) hat.
Diese Objekte sind die Bausteine unserer Programme, die wir mit Python schreiben.

Was ist aber, wenn wir unsere eigenen Objekte gestalten wollen (und wieso sollten wir das überhaupt wollen)?

## Objekte selbst gestalten

Beginnen wir bei unserem laufenden Beispiel, das ich in der Einleitung skizziert habe. Wir wollen ein Kartenspiel programmieren, genauer gesagt eine Poker-Variante, das man online gemeinsam und gegen einen KI-Gegner spielen kann.

Was sind die Grundbausteine eines Kartenspiels? Natürlich die Karten, oder? In unserem Programm können wir ohne diese Bausteine nicht auskommen. Jede Karte in einem "normalen" Kartenspiel (man denke an das französiche Blatt, das wir beim Poker brauchen) hat eine **Namen/Bezeichner** (z.B. "Ass"), einen **Wert** (z.B. 11 Punkte für den "Buben") und eine **Farbe** (z.B. Pik, Herz, etc.). Wir müssen diese Karten irgendwie modellieren. Wenn wir nun nicht wüssten, wie wir Objekte in Python bauen können, wie würden wir dann eine Karte, bzw. einen Stapel an Karten modellieren? Wahrscheinlich würden wir auf die einfachen Python Datenstrukturen, die wir kennen zurückgreifen. Vielleicht würden wir dazu ein Gemenge an Tupeln oder Dictionaries und Listen verwenden. Das Ganze könnte dann so aussehen:

```

