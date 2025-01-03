# kdtree obiektowo, ale jedynie liście zawierają punkty

# kdtree obiektowo, opcja w której wierzchołki zawierają punkty

from quicksort import quicksort


class KDtree:
    class Vertex:
        def __init__(self, point, left=None, right=None):
            self.point = point
            self.left = None
            self.right = None




    def __init__(self,points):
        xpoints = self.sort_by_dim(points,0)
        ypoints = self.sort_by_dim(points,1)
        self.root = self.build_tree(xpoints,ypoints,0)

    def get_root(self):
        return self.root

    def sort_by_dim(self,points,dim):
        sorted_points = points[:]
        quicksort(sorted_points, 0, len(points) - 1, dim)
        return sorted_points

    def divide_points(self,xpoints,ypoints,dim):
        if dim % 2 == 0:
            if not xpoints:
                return None
            if len(xpoints) == 1:
                return xpoints[0], [], [], [], []
            median = xpoints[(len(xpoints)-1) // 2][0]
            median_point = xpoints[(len(xpoints)-1) // 2]
            leftx = [point for point in xpoints if point[0] <= median]
            rightx = [point for point in xpoints if point[0] > median]
            lefty = [point for point in ypoints if point[0] <= median]
            righty = [point for point in ypoints if point[0] > median]
        else:
            if not ypoints:
                return None
            if len(ypoints) == 1:
                return ypoints[0], [], [], [], []
            median = ypoints[(len(ypoints)-1) // 2 ][1]
            median_point = ypoints[(len(ypoints)-1) // 2 ]
            leftx = [point for point in xpoints if point[1] <= median]
            rightx = [point for point in xpoints if point[1] > median]
            lefty = [point for point in ypoints if point[1] <= median]
            righty = [point for point in ypoints if point[1] > median]
        return median_point, leftx, rightx, lefty, righty


    def build_tree(self,xpoints,ypoints,depth):
        if depth % 2 == 0:
            # if not xpoints:
            #     return None
            if len(xpoints) == 1:
                return self.Vertex(xpoints[0])
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
        if root is None:
            return []
        if depth % 2 == 0:
            if area[0][0] <= root.point[0]:
                left = self.search_area(area,root.left,depth+1)
            else:
                left = []
            if area[1][0] >= root.point[0]:
                right = self.search_area(area,root.right,depth+1)
            else:
                right = []
        else:
            if area[0][1] <= root.point[1]:
                left = self.search_area(area,root.left,depth+1)
            else:
                left = []
            if area[1][1] >= root.point[1]:
                right = self.search_area(area,root.right,depth+1)
            else:
                right = []
        if area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1] and not root.left and not root.right:
            return left + [root.point] + right
        else:
            return left + right


test_data = [(1,1),(2,3),(0.5,4),(5.5,4.5),(6,2),(4,2.5),(3.5,6),(4.5,3.5)]
kdtree = KDtree(test_data)
#print(kdtree.get_root().left.right.right.point)
print(kdtree.search_area([(2,2),(6,6)],kdtree.get_root(),0)) # [(2, 3), (4, 2.5), (4.5, 3.5), (5.5, 4.5), (3.5, 6), (6, 2)]