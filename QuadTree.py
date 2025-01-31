class Point:
    """
    Klasa reprezentująca punkt na płaszczyźnie.
    """
    """Konstruktor punktu"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"  # Wypisanie punktu

class QuadTreeNode:
    """
    Węzeł w drzewie QuadTree przechowujący:
      - granice obszaru (x_min, y_min, x_max, y_max),
      - listę punktów (jeśli jest liściem),
      - odnośniki do dzieci: NW, NE, SW, SE.
    """

    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min  # lewy dolny rog wezla
        self.y_min = y_min  # lewy dolny rog wezla
        self.x_max = x_max  # prawy gorny rog wezla
        self.y_max = y_max  # prawy gorny rog wezla

        # Punkty przechowywane w tym węźle (tylko jeśli jest liściem bo jeśli nie jest liściem to ma dzieci i nie ma punktów )
        self.points = []

        # Dzieci: kolejność (NW, NE, SW, SE), podział na 4 części zgodnie z zasadą tworzenia Quad Tree
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None

        # Informacja, czy węzeł jest liściem (ma dzieci czy nie)
        self.is_leaf = True


class QuadTree:
    """
    Klasa zarządzająca QuadTree:
      - posiada korzeń (root),
      - operacje insert (wstawianie punktu),
      - operacje query_range (wyszukiwanie punktów w zadanym prostokącie).
    """

    def __init__(self, x_min, y_min, x_max, y_max, capacity=4):
        """
        Tworzy korzeń drzewa z zadaną pojemnością liścia (capacity),
        która określa maksymalną liczbę punktów przed podziałem.
        """
        self.root = QuadTreeNode(x_min, y_min, x_max, y_max)
        self.capacity = capacity  # maksymalna liczba punktów w węźle przed podziałem czyli 4

    def insert(self, node, point):
        """
        Wstawia punkt do drzewa, zaczynając od podanego węzła `node`.
        """
        # Jeśli węzeł jest liściem
        if node.is_leaf:
            # Jeśli jest jeszcze miejsce, to dodaj punkt
            if len(node.points) < self.capacity:
                node.points.append(point)
                return
            else:
                # Przekroczono pojemność -> podział
                self.subdivide(node)

                # Przenieś istniejące punkty do odpowiednich dzieci
                while node.points:
                    p = node.points.pop()
                    self.insert_into_child(node, p)

                # Teraz wstawiany punkt również ląduje w odpowiednim dziecku
                self.insert_into_child(node, point)

        else:
            # Jeśli węzeł nie jest liściem -> rekurencyjnie wstaw do dziecka
            self.insert_into_child(node, point)

    def insert_into_child(self, node, point):
        """
        Pomocnicza funkcja określająca, do którego dziecka węzła wstawić dany punkt. obliczamy srodek prostokata
        """
        mid_x = (node.x_min + node.x_max) / 2.0
        mid_y = (node.y_min + node.y_max) / 2.0

        # W zależności od położenia punktu wybieramy NW, NE, SW lub SE
        if point.x <= mid_x and point.y >= mid_y:
            # NW
            self.insert(node.nw, point)
        elif point.x > mid_x and point.y >= mid_y:
            # NE
            self.insert(node.ne, point)
        elif point.x <= mid_x and point.y < mid_y:
            # SW
            self.insert(node.sw, point)
        else:
            # SE
            self.insert(node.se, point)

    def subdivide(self, node):
        """
        Dzieli węzeł (node) na 4 dzieci: NW, NE, SW, SE.
        """
        mid_x = (node.x_min + node.x_max) / 2.0
        mid_y = (node.y_min + node.y_max) / 2.0

        # Tworzymy 4 podwęzły
        # NW
        node.nw = QuadTreeNode(
            x_min=node.x_min,
            y_min=mid_y,
            x_max=mid_x,
            y_max=node.y_max
        )
        # NE
        node.ne = QuadTreeNode(
            x_min=mid_x,
            y_min=mid_y,
            x_max=node.x_max,
            y_max=node.y_max
        )
        # SW
        node.sw = QuadTreeNode(
            x_min=node.x_min,
            y_min=node.y_min,
            x_max=mid_x,
            y_max=mid_y
        )
        # SE
        node.se = QuadTreeNode(
            x_min=mid_x,
            y_min=node.y_min,
            x_max=node.x_max,
            y_max=mid_y
        )

        node.is_leaf = False

    def query_range(self, node, x1, y1, x2, y2, found_points):  #
        """
        Wyszukuje punkty w zadanego prostokąta [x1, x2] x [y1, y2],
        zaczynając od węzła `node`.

        Wyniki dokłada do listy `found_points`.
        """
        # Jeśli nie ma przecięcia obszarów, to kończymy bo
        if not self.intersects(node, x1, y1, x2, y2):
            return

        # Jeśli węzeł jest liściem, to sprawdź wszystkie punkty
        if node.is_leaf:
            for p in node.points:
                if (x1 <= p.x <= x2) and (y1 <= p.y <= y2):
                    found_points.append(p)
        else:
            # Przeszukaj rekurencyjnie dzieci
            self.query_range(node.nw, x1, y1, x2, y2, found_points)
            self.query_range(node.ne, x1, y1, x2, y2, found_points)
            self.query_range(node.sw, x1, y1, x2, y2, found_points)
            self.query_range(node.se, x1, y1, x2, y2, found_points)

    def intersects(self, node, x1, y1, x2, y2):
        """
        Sprawdza, czy obszar węzła [x_min, x_max] x [y_min, y_max]
        nachodzi na [x1, x2] x [y1, y2].
        """
        return not (node.x_max < x1 or node.x_min > x2 or
                    node.y_max < y1 or node.y_min > y2)

    def insert_point(self, x, y):
        """
        Publiczna metoda wstawiania punktu (x, y) do całego drzewa.
        """
        p = Point(x, y)
        self.insert(self.root, p)

    def query(self, x1, y1, x2, y2):
        """
        Publiczna metoda wyszukiwania punktów w prostokącie (x1, y1, x2, y2).
        Zwraca listę znalezionych punktów.
        """
        found_points = []
        self.query_range(self.root, x1, y1, x2, y2, found_points)
        return change(found_points)

def find_end_points(points):
    x_min = float('inf')
    x_max = float('-inf')
    y_min = float('inf')
    y_max = float('-inf')

    for x, y in points:
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    return x_min, y_min, x_max, y_max


def CreateQuad(points_to_insert):
    qt = QuadTree(find_end_points(points_to_insert)[0], find_end_points(points_to_insert)[1],
                  find_end_points(points_to_insert)[2], find_end_points(points_to_insert)[3], capacity=4)
    for (x, y) in points_to_insert:
        qt.insert_point(x, y)
    return qt

def change(result):
    new_result = []
    for i in range(len(result)):
        new_result.append((result[i].x, result[i].y))
    return new_result



#points_to_insert = [(10, 10), (20, 90), (50, 50), (60, 60), (15, 15), (80, 95), (30, 70), (25, 200)]
# QT = CreateQuad(points_to_insert)
# result = change(QT.query(0, 0, 50, 50))
#print(f"Punkty w prostokącie [{x1},{y1}] x [{x2},{y2}]:")
# for p in result:
#     print(p)
