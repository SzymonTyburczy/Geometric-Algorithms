# kdtree obiektowo, ale jedynie liście zawierają punkty

# kdtree obiektowo, opcja w której wierzchołki zawierają punkty

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




    # def __init__(self,points):
    #     xpoints = self.sort_by_dim(points,0)
    #     ypoints = self.sort_by_dim(points,1)
    #     self.root = self.build_tree(xpoints,ypoints,0)

    def __init__(self,points):
        new_points = []
        for i in range(2):
            new_points.append(self.sort_by_dim(points,i))
        self.root = self.build_tree2(new_points,0)


    def get_root(self):
        return self.root

    @staticmethod
    def sort_by_dim(points, dim):
        sorted_points = points[:]
        quicksort(sorted_points, 0, len(points) - 1, dim)
        return sorted_points

    # def divide_points(self,xpoints,ypoints,dim):
    #     if dim % 2 == 0:
    #         if not xpoints:
    #             return None
    #         if len(xpoints) == 1:
    #             return xpoints[0], [], [], [], []
    #         median = xpoints[(len(xpoints)-1) // 2][0]
    #         median_point = xpoints[(len(xpoints)-1) // 2]
    #         leftx = [point for point in xpoints if point[0] <= median]
    #         rightx = [point for point in xpoints if point[0] > median]
    #         lefty = [point for point in ypoints if point[0] <= median]
    #         righty = [point for point in ypoints if point[0] > median]
    #     else:
    #         if not ypoints:
    #             return None
    #         if len(ypoints) == 1:
    #             return ypoints[0], [], [], [], []
    #         median = ypoints[(len(ypoints)-1) // 2 ][1]
    #         median_point = ypoints[(len(ypoints)-1) // 2 ]
    #         leftx = [point for point in xpoints if point[1] <= median]
    #         rightx = [point for point in xpoints if point[1] > median]
    #         lefty = [point for point in ypoints if point[1] <= median]
    #         righty = [point for point in ypoints if point[1] > median]
    #     return median_point, leftx, rightx, lefty, righty
    #
    #
    # def build_tree(self,xpoints,ypoints,depth):
    #     if depth % 2 == 0:
    #         # if not xpoints:
    #         #     return None
    #         if len(xpoints) == 1:
    #             return self.Vertex(xpoints[0])
    #         division = self.divide_points(xpoints, ypoints, depth)
    #         if division:
    #             median, leftx, rightx, lefty, righty = division
    #         else:
    #             return None
    #     else:
    #         if not ypoints:
    #             return None
    #         if len(ypoints) == 1:
    #             return self.Vertex(ypoints[0])
    #         division = self.divide_points(xpoints, ypoints, depth)
    #         if division:
    #             median, leftx, rightx, lefty, righty = division
    #         else:
    #             return None
    #     root = self.Vertex(median)
    #     root.left = self.build_tree(leftx,lefty,depth+1)
    #     root.right = self.build_tree(rightx,righty,depth+1)
    #     return root

    def divide_points2(self,points,dim):
        if not points[dim]:
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
        # print(median_point)
        # print(left,right)
        return median_point, left, right

    def build_tree2(self,points,depth):
        dim = depth % 2
        # print(depth)
        # print(points)
        if len(points[dim]) == 1:
            return self.Leaf(points[dim][0])
        division = self.divide_points2(points,dim)
        if division:
            median, left, right = division
        else:
            return None
        root = self.Vertex(median[dim])
        root.left = self.build_tree2(left,depth+1)
        root.right = self.build_tree2(right,depth+1)
        return root


    # def search_area(self,area,root,depth):
    #     if root is None:
    #         return []
    #     if depth % 2 == 0:
    #         if area[0][0] <= root.point[0]:
    #             left = self.search_area(area,root.left,depth+1)
    #         else:
    #             left = []
    #         if area[1][0] >= root.point[0]:
    #             right = self.search_area(area,root.right,depth+1)
    #         else:
    #             right = []
    #     else:
    #         if area[0][1] <= root.point[1]:
    #             left = self.search_area(area,root.left,depth+1)
    #         else:
    #             left = []
    #         if area[1][1] >= root.point[1]:
    #             right = self.search_area(area,root.right,depth+1)
    #         else:
    #             right = []
    #     if area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1] and not root.left and not root.right:
    #         return left + [root.point] + right
    #     else:
    #         return left + right

    def search_area2(self,area,root,depth):
        if root is None:
            return []
        left = []
        right = []
        if root.getclass() == self.Vertex:
            dim = depth % 2
            if area[0][dim] <= root.divider:
                left = self.search_area2(area,root.left,depth+1)
            else:
                left = []
            if area[1][dim] >= root.divider:
                right = self.search_area2(area,root.right,depth+1)
            else:
                right = []
        else:
            if root.getclass() == self.Leaf and area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1]:
                return left + [root.point] + right
        return left + right


test_data = [(1,1),(2,3),(0.5,4),(5.5,4.5),(6,2),(4,2.5),(3.5,6),(4.5,3.5)]
kdtree = KDtree(test_data)
# print(kdtree.get_root().left.left.right.point)
#print(kdtree.search_area2([(3,3),(6,6)],kdtree.get_root(),0)) # [(2, 3), (4, 2.5), (4.5, 3.5), (5.5, 4.5), (3.5, 6), (6, 2)]

