from quicksort import quicksort, quicksort_np
import numpy as np


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

    # @staticmethod
    # def area_in_bounds(area,bounds):
    #     if area[0][0] >= bounds[0][0] and area[0][1] >= bounds[0][1] and area[1][0] <= bounds[1][0] and area[1][1] <= bounds[1][1]:
    #         return True
    #     return False
    #
    # @staticmethod
    # def bounds_in_area(area,bounds):
    #     if bounds[0][0] >= area[0][0] and bounds[0][1] >= area[0][1] and bounds[1][0] <= area[1][0] and bounds[1][1] <= area[1][1]:
    #         return True
    #     return False
    #
    # def add_all_points(self,root,result):
    #     if root is None:
    #         return []
    #     if root.getclass() == self.Leaf:
    #         result.append(root.point)
    #     else:
    #         self.add_all_points(root.left,result)
    #         self.add_all_points(root.right,result)
    #
    # def search_area_bb(self, area, root, depth,result,bounds = ((-float("inf"),-float("inf")),(float("inf"),float("inf")))):
    #     if root is None:
    #         return []
    #     if root.getclass() == self.Vertex:
    #         dim = depth % 2
    #         if dim == 0:
    #             left_bounds = ((bounds[0][0], bounds[0][1]), (root.divider, bounds[1][1]))
    #             right_bounds = ((root.divider, bounds[0][1]), (bounds[1][0], bounds[1][1]))
    #         else:
    #             left_bounds = ((bounds[0][0], bounds[0][1]), (bounds[1][0], root.divider))
    #             right_bounds = ((bounds[0][0], root.divider), (bounds[1][0], bounds[1][1]))
    #
    #         if self.bounds_in_area(area,left_bounds):
    #             self.add_all_points(root.left,result)
    #         elif self.bounds_in_area(area,right_bounds):
    #             self.add_all_points(root.right,result)
    #         elif self.area_in_bounds(area,left_bounds):
    #             self.search_area_bb(area,root.left,depth+1,result,left_bounds)
    #         elif self.area_in_bounds(area,right_bounds):
    #             self.search_area_bb(area,root.right,depth+1,result,right_bounds)
    #         else:
    #             self.search_area_bb(area,root.left,depth+1,result,left_bounds)
    #             self.search_area_bb(area,root.right,depth+1,result,right_bounds)
    #     else:
    #         if root.getclass() == self.Leaf and area[0][0] <= root.point[0] <= area[1][0] and area[0][1] <= root.point[1] <= area[1][1]:
    #             result.append(root.point)


# test_data = [(1,1),(2,3),(0.5,4),(5.5,4.5),(6,2),(4,2.5),(3.5,6),(4.5,3.5)]
# kdtree = KDtree(test_data)
# print(kdtree.get_root().left.left.right.point)
# print(kdtree.search_area2([(2,2),(6,6)],kdtree.get_root(),0)) # [(2, 3), (4, 2.5), (4.5, 3.5), (5.5, 4.5), (3.5, 6), (6, 2)]
# result = []
# kdtree.search_area_bb([(3,3),(6,6)],kdtree.get_root(),0,result)
# print(result)
# test = np.array(test_data)
# kdtree = KDtree(test)
# print(kdtree.get_root().left.divider)
# print(kdtree.search_area([(2,2),(6,6)],kdtree.get_root(),0)) # [(2, 3), (4, 2.5), (4.5, 3.5), (5.5, 4.5), (3.5, 6), (6, 2)]
# result_np = []
# kdtree.search_area_bb([(3,3),(6,6)],kdtree.get_root(),0,result_np) # [(4, 2.5), (4.5, 3.5), (5.5, 4.5), (3.5, 6), (6, 2)]
# print(result_np)