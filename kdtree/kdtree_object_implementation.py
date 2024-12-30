# kdtree obiektowo

from quicksort import quicksort

class KDtree:
    def __init__(self):
        self.root = None

    class Vertex:
        def __init__(self, point, left=None, right=None):
            self.point = point
            self.left = None
            self.right = None

