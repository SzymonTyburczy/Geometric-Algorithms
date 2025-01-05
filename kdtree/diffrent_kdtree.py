
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
        self.root = self.build_tree(xpoints,ypoints,0)

    def get_root(self):
        return self.root

    @staticmethod
    def sort_by_dim(points, dim):
        sorted_points = points[:]
        sorted(sorted_points, key=lambda x: x[dim])
        return sorted_points

    def divide_points(self,xpoints,ypoints,dim):
        if dim % 2 == 0:
            if not xpoints:
                return None
            if len(xpoints) == 1:
                return xpoints[0], [], [], [], []
            median = xpoints[(len(xpoints)-1) // 2][0]
            median_point = xpoints[(len(xpoints)-1) // 2]
            leftx = [point for point in xpoints if (point[0] <= median and point != median_point)]
            rightx = [point for point in xpoints if point[0] > median]
            lefty = [point for point in ypoints if (point[0] <= median and point != median_point)]
            righty = [point for point in ypoints if point[0] > median]
        else:
            if not ypoints:
                return None
            if len(ypoints) == 1:
                return ypoints[0], [], [], [], []
            median = ypoints[(len(ypoints)-1) // 2 ][1]
            median_point = ypoints[(len(ypoints)-1) // 2 ]
            leftx = [point for point in xpoints if (point[1] <= median and point != median_point)]
            rightx = [point for point in xpoints if point[1] > median]
            lefty = [point for point in ypoints if (point[1] <= median and point != median_point)]
            righty = [point for point in ypoints if point[1] > median]
        return median_point, leftx, rightx, lefty, righty


    def build_tree(self,xpoints,ypoints,depth):
        if depth % 2 == 0:
            if not xpoints:
                return None
            if len(xpoints) == 1:
                return self.Leaf(xpoints[0])
            division = self.divide_points(xpoints, ypoints, depth)
            if division:
                median, leftx, rightx, lefty, righty = division
            else:
                return None
        else:
            if not ypoints:
                return None
            if len(ypoints) == 1:
                return self.Vertex(ypoints[0])
            division = self.divide_points(xpoints, ypoints, depth)
            if division:
                median, leftx, rightx, lefty, righty = division
            else:
                return None
        root = self.Vertex(median)
        root.left = self.build_tree(leftx,lefty,depth+1)
        root.right = self.build_tree(rightx,righty,depth+1)
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

