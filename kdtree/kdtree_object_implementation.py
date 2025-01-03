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

    @staticmethod
    def sort_by_dim(points, dim):
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
        dim = depth % 2
        if root is None:
            return []
        if area[0][dim] <= root.point[dim]:
            left = self.search_area(area,root.left,depth+1)
        else:
            left = []
        if area[1][dim] >= root.point[dim]:
            right = self.search_area(area,root.right,depth+1)
        else:
            right = []
        if area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1]:
            return left + [root.point] + right
        else:
            return left + right

    @staticmethod
    def area_in_bounds(area, bounds):
        if area[0][0] >= bounds[0][0] and area[0][1] >= bounds[0][1] and area[1][0] <= bounds[1][0] and area[1][1] <= bounds[1][1]:
            # print(area,bounds)
            return True
        return False

    @staticmethod
    def bounds_in_area(area,bounds):
        if bounds[0][0] >= area[0][0] and bounds[0][1] >= area[0][1] and bounds[1][0] <= area[1][0] and bounds[1][1] <= area[1][1]:
            # print(bounds,area)
            return True
        return False

    def add_all_points(self,root,result):
        if root is None:
            return []
        result.append(root.point)
        self.add_all_points(root.left,result)
        self.add_all_points(root.right,result)

# wyszukiwanie z box bounding
    def search_area_bb(self,area,root,result,depth,bounds = ((float("-inf"),float("-inf")),(float("inf"),float("inf")))):
        dim = depth % 2
        if root is None:
            return []
        # print(root.point, depth)

        if area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1]:
            result.append(root.point)
        if dim == 0:
            left_bounds = ((bounds[0][0],bounds[0][1]),(root.point[0],bounds[1][1]))
            right_bounds = ((root.point[0],bounds[0][1]),(bounds[1][0],bounds[1][1]))
        else:
            left_bounds = ((bounds[0][0], bounds[0][1]), (bounds[1][0], root.point[1]))
            right_bounds = ((bounds[0][0], root.point[1]), (bounds[1][0], bounds[1][1]))
        # print(left_bounds)
        # print(right_bounds)
        # print(result)


        if self.area_in_bounds(area,left_bounds):
            # print("left")
            if self.bounds_in_area(area,left_bounds):
                self.add_all_points(root.left,result)
            else:
                self.search_area_bb(area,root.left,result,depth+1,left_bounds)
        elif self.area_in_bounds(area,right_bounds):
            # print("right")
            if self.bounds_in_area(area,right_bounds):
                self.add_all_points(root.right,result)
            else:
                self.search_area_bb(area,root.right,result,depth+1,right_bounds)

        else:
            if area[0][dim] <= root.point[dim] <= area[1][dim]:
                self.search_area_bb(area,root.left,result,depth+1,left_bounds)
                self.search_area_bb(area,root.right,result,depth+1,right_bounds)


# test_data = [(1,1),(2,3),(0.5,4),(5.5,4.5),(6,2),(4,2.5),(3.5,6),(4.5,3.5)]
# kdtree = KDtree(test_data)
# print(kdtree.get_root().left.right.right.point)
# print(kdtree.search_area([(2,2),(6,6)],kdtree.get_root(),0)) # [(2, 3), (4, 2.5), (4.5, 3.5), (5.5, 4.5), (3.5, 6), (6, 2)]
# result = []
# kdtree.search_area_bb([(2,2),(6,6)],kdtree.get_root(),result,0)
# print(result) # [(2, 3), (4, 2.5), (4.5, 3.5), (5.5, 4.5), (3.5, 6), (6, 2)]
# new_result = []
# kdtree.search_area_bb([(5,4),(6,6)],kdtree.get_root(),new_result,0)
# print(new_result) # [(5.5, 4.5)]
# print(kdtree.search_area([(5,4),(6,6)],kdtree.get_root(),0)) # [(5.5, 4.5)]
