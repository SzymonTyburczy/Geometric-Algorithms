
class KDtree:
    def __init__(self,points):
        xpoints = self.sort_by_dim(points,0)
        ypoints = self.sort_by_dim(points,1)
        self.root = self.build_tree([xpoints,ypoints],0)

    class Vertex:
        def __init__(self, point, left=None, right=None):
            self.point = point
            self.left = left
            self.right = right

        def getclass(self):
            return self.__class__

    class Leaf:
        def __init__(self, point):
            self.point = point

        def getclass(self):
            return self.__class__


    def get_root(self):
        return self.root

    @staticmethod
    def sort_by_dim(points, dim):
        # stworzenie kopii zbioru punktów
        sorted_points = points[:]
        # sortowanie punktów względem wybranej współrzędnej
        sorted(sorted_points, key=lambda x: x[dim])
        # zwrócenie posortowanych punktów
        return sorted_points


# metoda dzieląca zbiór punktów na zbiory lewy i prawy
# jako argumenty przyjmuje zbiór punktów oraz wybraną współrzędną
    def divide_points(self,points,dim):
        # sprawdzenie czy zbiór punktów nie jest pusty
        if not points[dim]:
            return None
        # sprawdzenie czy zbiór punktów zawiera tylko jeden punkt
        if len(points[dim]) == 1:
            return points[dim][0], [], []
        # wyznaczenie mediany punktów względem wybranej współrzędnej
        median = points[dim][(len(points[dim]) - 1) // 2][dim]
        median_point = points[dim][(len(points[dim]) - 1) // 2]
        # stworzenie dwóch zbiorów punktów: lewego i prawego
        left = []
        right = []
        # podział punktów na zbiory lewy i prawy
        for i in range(2):
            left_points = [point for point in points[i] if (point[dim] <= median and point != median_point)]
            right_points = [point for point in points[i] if point[dim] > median]
            left.append(left_points)
            right.append(right_points)
        # zwrócenie mediany punktów oraz zbiorów lewego
        return median_point, left, right

# metoda budująca drzewo KD
    def build_tree(self,points,depth):
        # wyznaczenie współrzędnej, względem której dokonujemy podziału
        dim = depth % 2
        # sprawdzenie czy zbiór punktów zawiera tylko jeden punkt
        # jeśli tak, zwracamy liść z tym punktem
        if len(points[dim]) == 1:
            return self.Leaf(points[dim][0])
        # podział zbioru punktów na zbiory lewy i prawy
        division = self.divide_points(points, dim)
        # jeśli podział istnieje, to wyznaczamy medianę punktów, lewy i prawy zbiór
        if division:
            median, left, right = division
        else:
            return None
        # stworzenie wierzchołka drzewa KD
        root = self.Vertex(median)
        # rekurencyjne wywołanie metody build_tree dla zbiorów lewego i prawego
        root.left = self.build_tree(left, depth + 1)
        root.right = self.build_tree(right, depth + 1)
        # zwrócenie korzenia drzewa KD
        return root


# metoda wyszukująca punkty w zadanym obszarze
    def search_area(self,area,root,depth):
        # wyznaczenie współrzędnej, względem której dokonujemy podziału
        dim = depth % 2
        # sprawdzenie czy korzeń drzewa nie jest pusty
        if root is None:
            return []
        # sprawdzenie czy korzeń drzewa jest klasy Vertex
        if root.getclass() == self.Vertex:
            # stworzenie dwóch zbiorów punktów: lewego i prawego
            left = []
            right = []
            # sprawdzenie czy obszar przecina się z lewym i prawym poddrzewem
            if root.point[dim]>= area[0][dim]:
                left = self.search_area(area,root.left,depth+1)
            if root.point[dim]<= area[1][dim]:
                right = self.search_area(area,root.right,depth+1)
            # sprawdzenie czy korzeń drzewa należy do zadanego obszaru
            if area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1]:
                return left + [root.point] + right
            else:
                return left + right
        else:
            # sprawdzenie czy liść należy do zadanego obszaru
            if (area[0][0] <= root.point[0] <= area[1][0]) and (area[0][1] <= root.point[1] <= area[1][1]):
                return [root.point]
            return []

