
class KDtree:
    class Vertex:
        def __init__(self, point, left=None, right=None):
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

    def __init__(self,points):
        xpoints = self.sort_by_dim(points,0)
        ypoints = self.sort_by_dim(points,1)
        self.root = self.build_tree([xpoints,ypoints],0)

    def get_root(self):
        return self.root

    @staticmethod
    def sort_by_dim(points, dim):
        sorted_points = points[:]
        sorted(sorted_points, key=lambda x: x[dim])
        return sorted_points


    def divide_points(self,points,dim):
        if not points[dim]:
            return None
        if len(points[dim]) == 1:
            return points[dim][0], [], []
        median = points[dim][(len(points[dim]) - 1) // 2][dim]
        median_point = points[dim][(len(points[dim]) - 1) // 2]
        left = []
        right = []
        for i in range(2):
            left_points = [point for point in points[i] if (point[dim] <= median and point != median_point)]
            right_points = [point for point in points[i] if point[dim] > median]
            left.append(left_points)
            right.append(right_points)
        return median_point, left, right

    def build_tree(self,points,depth):
        dim = depth % 2
        if len(points[dim]) == 1:
            return self.Leaf(points[dim][0])
        division = self.divide_points(points, dim)
        if division:
            median, left, right = division
        else:
            return None
        root = self.Vertex(median)
        root.left = self.build_tree(left, depth + 1)
        root.right = self.build_tree(right, depth + 1)
        return root


    def search_area(self,area,root,depth):
        dim = depth % 2
        if root is None:
            return []

        if root.getclass() == self.Vertex:
            left = []
            right = []

            if root.point[dim]>= area[0][dim]:
                left = self.search_area(area,root.left,depth+1)
            if root.point[dim]<= area[1][dim]:
                right = self.search_area(area,root.right,depth+1)

            if area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1]:
                return left + [root.point] + right
            else:
                return left + right
        else:
            if (area[0][0] <= root.point[0] <= area[1][0]) and (area[0][1] <= root.point[1] <= area[1][1]):
                return [root.point]
            return []

