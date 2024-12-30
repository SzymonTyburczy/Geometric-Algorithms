# Implementacja struktury kdtree dla 2 wymiarów (2dtree), wszystkie wierzchołki zawierają punkty.
# Raczej nie nadaje się najlepiej do wyszukiwania punktów w obszarze, ale do znajdowania najbliższego punktu

# nie działa

from quicksort import quicksort

class Vertex:
    def __init__(self,point,left=None,right=None):
        self.point = point
        self.left = None
        self.right = None

def divide_points(xpoints,ypoints,dim):
    if dim % 2 == 0:
        if len(xpoints) == 0:
            return None
        elif len(xpoints) == 1:
            return xpoints[0], [], [], [], []
        median = xpoints[(len(xpoints)-1) // 2 ][0]
        median_point = xpoints[(len(xpoints)-1) // 2]
        print("median: ", median_point)
        leftx = [point for point in xpoints if (point[0] <= median and point != median_point)]
        rightx = [point for point in xpoints if point[0] > median]
        lefty = [point for point in ypoints if (point[0] <= median and point != median_point)]
        righty = [point for point in ypoints if point[0] > median]
    else:
        if len(ypoints) == 0:
            return None
        elif len(ypoints) == 1:
            return ypoints[0], [], [], [], []
        median = ypoints[(len(ypoints)-1) // 2][1]
        median_point = ypoints[(len(ypoints)-1) // 2 ]
        print("median: ", median_point)
        leftx = [point for point in xpoints if (point[1] <= median and point != median_point)]
        rightx = [point for point in xpoints if point[1] > median]
        lefty = [point for point in ypoints if (point[1] <= median and point != median_point)]
        righty = [point for point in ypoints if point[1] > median]
    return median_point, leftx, rightx, lefty, righty

def sort_by_dim(points,dim):
    sorted_points = points[:]
    quicksort(sorted_points,0,len(points)-1,dim)
    return sorted_points


def kdtree_init(points):
    x_sorted = sort_by_dim(points, 0)
    y_sorted = sort_by_dim(points, 1)

    # def build_kdtree(xpoints, ypoints, depth):
    #     print("depth: ", depth)
    #     print(xpoints)
    #     print(ypoints)
    #     # if len(points) == 0:
    #     #     return None
    #     # if len(points) == 1:
    #     #     return points[0]
    #     if depth % 2 == 0:
    #         if len(xpoints) == 0:
    #             return None
    #         if len(xpoints) == 1:
    #             return Vertex(xpoints[0])
    #         division = divide_points(xpoints, ypoints, depth)
    #         if division:
    #             point, leftx, rightx, lefty, righty = division
    #         else:
    #             return None
    #         # leftP = None  # points smaller or equal to median x
    #         # rightP = None  # points greater than median x
    #     else:
    #         if len(ypoints) == 0:
    #             return None
    #         if len(ypoints) == 1:
    #             return Vertex(ypoints[0])
    #         division = divide_points(xpoints, ypoints, depth)
    #         if division:
    #             point, leftx, rightx, lefty, righty = division
    #         else:
    #             return None
    #
    #     return Vertex(point, build_kdtree(leftx, lefty, depth + 1), build_kdtree(rightx, righty, depth + 1))

    def build_kdtree(xpoints, ypoints, depth):
        print("depth: ", depth)
        print(xpoints)
        print(ypoints)

        if len(xpoints) == 1:
            return Vertex(xpoints[0])
        if len(ypoints) == 1:
            return Vertex(ypoints[0])

        division = divide_points(xpoints, ypoints, depth)
        if not division:
            return Vertex(None)

        point, leftx, rightx, lefty, righty = division

        left_child = build_kdtree(leftx, lefty, depth + 1)
        right_child = build_kdtree(rightx, righty, depth + 1)

        vertex = Vertex(point, left_child, right_child)
        print("vertex: ",vertex.point,vertex.left,vertex.right)

        return vertex

    return build_kdtree(x_sorted, y_sorted, 0)


test_data = [(1,1),(2,3),(0.5,4),(5.5,4.5),(6,2),(4,2.5),(3.5,6),(4.5,3.5)]
# test_data = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)]
# test_data = [(1,1),(1,4),(2,3),(6,2),(4,4),(2,7),(6,6),(8,4),(8,6)]
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
#print(kdtree.point)
#print(kdtree.left)