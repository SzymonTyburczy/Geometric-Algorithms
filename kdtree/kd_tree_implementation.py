# implementacja strukktury kdtree dla 2 wymiarów (2dtree)

from quicksort import quicksort
from copy import deepcopy

class Vertex:
    def __init__(self,point,left=None,right=None):
        self.point = point
        self.left = None
        self.right = None

def divide_points(xpoints,ypoints,dim):
    if dim %2 == 0:
        if len(xpoints) == 0:
            return None,
        elif len(xpoints) == 1:
            return xpoints[0],[],[],[],[]
        median = xpoints[len(xpoints)//2][0]
        median_point = xpoints[len(xpoints)//2]
        print("median: ",median_point)
        leftx = [point for point in xpoints if (point[0] <= median and point != median_point)]
        rightx = [point for point in xpoints if point[0] > median]
        lefty = [point for point in ypoints if (point[0] <= median and point != median_point)]
        righty = [point for point in ypoints if point[0] > median]
    else:
        if len(ypoints) == 0:
            return None
        elif len(ypoints) == 1:
            return ypoints[0],[],[],[],[]
        median = ypoints[len(ypoints)//2][1]
        median_point = ypoints[len(ypoints)//2]
        print("median: ",median_point)
        leftx = [point for point in xpoints if (point[1] <= median and point != median_point)]
        rightx = [point for point in xpoints if point[1] > median]
        lefty = [point for point in ypoints if (point[1] <= median and point != median_point)]
        righty = [point for point in ypoints if point[1] > median]
    return median_point,leftx,rightx,lefty,righty

def sort_by_dim(points,dim):
    sorted_points = points[:]
    quicksort(sorted_points,0,len(points)-1,dim)
    return sorted_points


def kdtree_init(points):
    x_sorted = sort_by_dim(points,0)
    y_sorted = sort_by_dim(points,1)

    def build_kdtree(xpoints,ypoints, depth):
        print("depth: ",depth)
        print(xpoints)
        print(ypoints)
        # if len(points) == 0:
        #     return None
        # if len(points) == 1:
        #     return points[0]
        if depth % 2 == 0:
            if len(xpoints) == 0:
                return None
            if len(xpoints) == 1:
                return points[0]
            division = divide_points(xpoints, ypoints, depth)
            if division:
                point, leftx, rightx, lefty, righty = division
            else:
                return None
            # leftP = None  # points smaller or equal to median x
            # rightP = None  # points greater than median x
        else:
            if len(ypoints) == 0:
                return None
            if len(ypoints) == 1:
                return points[0]
            division = divide_points(xpoints, ypoints, depth)
            if division:
                point, leftx, rightx, lefty, righty = division
            else:
                return None
            # leftP = None  # points smaller or equal to median y
            # rightP = None  # points greater than median y

        vertex = Vertex(point, build_kdtree(leftx,lefty, depth + 1), build_kdtree(rightx,righty, depth + 1))

        # build_kdtree(leftP,depth+1),
        # build_kdtree(rightP,depth+1)
        # make vertex with median as root and leftP and rightP as children
        return vertex
        # return vertex
    return build_kdtree(x_sorted,y_sorted,0)

# def build_kdtree(points,depth):
#     if len(points) == 0:
#         return None
#     if len(points) == 1:
#         return points[0]
#     elif depth % 2 == 0:
#         median = find_median(points,0)
#         leftP = None # points smaller or equal to median x
#         rightP = None # points greater than median x
#     else:
#         median = find_median(points,1)
#         leftP = None # points smaller or equal to median y
#         rightP = None  # points greater than median y
#
#     vertex = Vertex(points[median],build_kdtree(leftP,depth+1),build_kdtree(rightP,depth+1))
#
#     # build_kdtree(leftP,depth+1),
#     # build_kdtree(rightP,depth+1)
#     # make vertex with median as root and leftP and rightP as children
#     return None # return vertex

test_data = [(1,1),(2,3),(0.5,4),(5.5,4.5),(6,2),(4,2.5),(3.5,6),(4.5,3.5)]
# xsorted  = sort_by_dim(test_data,0)
# ysorted = sort_by_dim(test_data,1)
# print(xsorted)
# print(ysorted)

# point,lx,rx,ly,ry = divide_points(xsorted,ysorted,0)
# print(point)
# print(lx)
# print(rx)
# print(ly)
# print(ry)

# point,lx,rx,ly,ry = divide_points(xsorted,ysorted,1)
# print(point)
# print(lx)
# print(rx)
# print(ly)
# print(ry)

kdtree = kdtree_init(test_data)
print(kdtree.point)