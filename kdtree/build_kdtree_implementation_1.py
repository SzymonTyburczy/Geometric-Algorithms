# implementacja build_kdtree, która zawiera punkty wyłącznie w liściach, a w wierzchołkach medianę dzielącą zbiór,
# czyli wirtualną prostą, która dzieli przestrzeń na dwie części

from quicksort import quicksort

class Vertex:
    def __init__(self,point,left=None,right=None):
        self.point = point
        self.left = None
        self.right = None

def sort_by_dim(points,dim):
    sorted_points = points[:]
    quicksort(sorted_points,0,len(points)-1,dim)
    return sorted_points

def divide_points(xpoints,ypoints,dim):
    if dim % 2 == 0:
        if len(xpoints) == 0:
            return None
        elif len(xpoints) == 1:
            return xpoints[0], [], [], [], []
        median = xpoints[len(xpoints) // 2 -1][0]
        median_point = xpoints[len(xpoints) // 2 -1]
        print("median: ", median_point)
        leftx = [point for point in xpoints if point[0] <= median]
        rightx = [point for point in xpoints if point[0] > median]
        lefty = [point for point in ypoints if point[0] <= median]
        righty = [point for point in ypoints if point[0] > median]
    else:
        if len(ypoints) == 0:
            return None
        elif len(ypoints) == 1:
            return ypoints[0], [], [], [], []
        median = ypoints[len(ypoints) // 2 - 1][1]
        median_point = ypoints[len(ypoints) // 2 -1]
        print("median: ", median_point)
        leftx = [point for point in xpoints if point[1] <= median]
        rightx = [point for point in xpoints if point[1] > median]
        lefty = [point for point in ypoints if point[1] <= median]
        righty = [point for point in ypoints if point[1] > median]
    return median_point, leftx, rightx, lefty, righty

def kdtree_init(points):
    x_sorted = sort_by_dim(points, 0)
    y_sorted = sort_by_dim(points, 1)

    def build_kdtree(xpoints,ypoints, depth):
        print("depth: ",depth)
        print(xpoints)
        print(ypoints)

        if depth % 2 == 0:
            if len(xpoints) == 0:
                return None
            if len(xpoints) == 1:
                return Vertex(xpoints[0])
            division = divide_points(xpoints, ypoints, depth)
            if division:
                median, leftx, rightx, lefty, righty = division
            else:
                return None

        else:
            if len(ypoints) == 0:
                return None
            if len(ypoints) == 1:
                return Vertex(ypoints[0])
            division = divide_points(xpoints, ypoints, depth)
            if division:
                median, leftx, rightx, lefty, righty = division
            else:
                return None

        vertex = Vertex(median, build_kdtree(leftx,lefty, depth + 1), build_kdtree(rightx,righty, depth + 1))

        return vertex

    return build_kdtree(x_sorted, y_sorted, 0)

test_data = [(1,1),(2,3),(0.5,4),(5.5,4.5),(6,2),(4,2.5),(3.5,6),(4.5,3.5)]
kdtree = kdtree_init(test_data)
print(kdtree.point)