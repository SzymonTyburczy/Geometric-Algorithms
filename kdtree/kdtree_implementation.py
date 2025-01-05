from quicksort import quicksort

class KDtree:
    class Vertex:
        def __init__(self, point, left=None, right=None):
            self.divider = point
            self.left = None
            self.right = None

        def getclass(self):
            return self.__class__

    class Leaf:
        def __init__(self, point):
            self.point = point

        def getclass(self):
            return self.__class__

    def __init__(self,points):
        new_points = []
        for i in range(2):
            new_points.append(self.sort_by_dim(points,i))
        self.root = self.build_tree(new_points,0)


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

    def build_tree(self,points,depth):
        dim = depth % 2
        if len(points[dim]) == 1:
            return self.Leaf(points[dim][0])
        division = self.divide_points(points,dim)
        if division:
            median, left, right = division
        else:
            return None
        root = self.Vertex(median[dim])
        root.left = self.build_tree(left,depth+1)
        root.right = self.build_tree(right,depth+1)
        return root


    def search_area(self,area,root,depth):
        if root is None:
            return []
        left = []
        right = []
        if root.getclass() == self.Vertex:
            dim = depth % 2
            if area[0][dim] <= root.divider:
                left = self.search_area(area,root.left,depth+1)
            else:
                left = []
            if area[1][dim] >= root.divider:
                right = self.search_area(area,root.right,depth+1)
            else:
                right = []
        else:
            if root.getclass() == self.Leaf and area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1]:
                return left + [root.point] + right
        return left + right

