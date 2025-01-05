from quicksort import quicksort, quicksort_np
import numpy as np


class KDtree:
    class Vertex:
        def __init__(self, point):
            # point to teraz PEŁNY punkt (np. (x, y)), a nie tylko x lub y
            self.point = point
            self.left = None
            self.right = None

        def getclass(self):
            return self.__class__

    class Leaf:
        def __init__(self, point):
            self.point = point

        def getclass(self):
            return self.__class__

    def __init__(self, points):
        # Zamieniamy ewentualne np.array na listę krotek, jeśli trzeba
        if isinstance(points, np.ndarray):
            points = [tuple(p) for p in points]
        self.root = self.build_tree(points, 0)

    def get_root(self):
        return self.root

    @staticmethod
    def sort_by_dim(points, dim):
        sorted_points = points[:]
        quicksort(sorted_points, 0, len(points) - 1, dim)
        return sorted_points

    def divide_points(self,points,dim):
        if len( points[dim])==0:
            return None
        if len(points[dim]) == 1:
            return points[dim][0], [], []
        median = points[dim][(len(points[dim])-1) // 2][dim]
        median_point = points[dim][(len(points[dim])-1) // 2]
        left = []
        right = []
        for i in range(2):
            left_points = [point for point in points[i] if point[dim] <= median]
            right_points = [point for point in points[i] if point[dim] > median]
            left.append(left_points)
            right.append(right_points)
        return median_point, left, right

    def build_tree(self, points, depth=0):
        if not points:
            return None
        if len(points) == 1:
            return self.Leaf(points[0])

        dim = depth % 2
        # Sortujemy punkty względem aktualnego wymiaru:
        points.sort(key=lambda p: p[dim])

        # Indeks mediany
        median_idx = len(points) // 2
        # Pobieramy punkt mediany
        median_point = points[median_idx]

        # Budujemy węzeł wewnętrzny z CAŁYM punktem
        root = self.Vertex(median_point)

        # Lewa i prawa część – bez punktu mediany
        left_points = points[:median_idx]
        right_points = points[median_idx + 1:]

        # Rekurencyjnie budujemy poddrzewa
        root.left = self.build_tree(left_points, depth + 1)
        root.right = self.build_tree(right_points, depth + 1)

        return root

    def search_area(self, area, root, depth=0):
        if root is None:
            return []

        # area = [(x_min, y_min), (x_max, y_max)]
        x_min, y_min = area[0]
        x_max, y_max = area[1]

        if root.getclass() == self.Vertex:
            # Punkt w węźle
            point = root.point
            dim = depth % 2
            # lewa / prawa rekursja
            left_res = []
            right_res = []

            # Jeśli wymiary pozwalają, idziemy w lewo:
            # porównujemy root.point[dim] z minimalnym i maksymalnym w danym wymiarze
            if point[dim] >= (x_min if dim == 0 else y_min):
                left_res = self.search_area(area, root.left, depth + 1)
            if point[dim] <= (x_max if dim == 0 else y_max):
                right_res = self.search_area(area, root.right, depth + 1)

            # Sprawdzamy, czy punkt w węźle sam w sobie leży w obszarze
            if (x_min <= point[0] <= x_max) and (y_min <= point[1] <= y_max):
                return left_res + [point] + right_res
            else:
                return left_res + right_res

        else:  # root jest liściem
            # Sprawdź, czy liść mieści się w obszarze
            p = root.point
            if (x_min <= p[0] <= x_max) and (y_min <= p[1] <= y_max):
                return [p]
            return []

