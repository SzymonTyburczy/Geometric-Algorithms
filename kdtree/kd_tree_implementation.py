# implementacja strukktury kdtree dla 2 wymiarów (2dtree)

class Vertex:
    def __init__(self,point,left=None,right=None):
        self.point = point
        self.left = None
        self.right = None

def find_median(points,depth):
    pass

def build_kdtree(points,depth):
    if len(points) == 0:
        return None
    if len(points) == 1:
        return points[0]
    elif depth % 2 == 0:
        median = find_median(points,0)
        leftP = None # points smaller or equal to median x
        rightP = None # points greater than median x
    else:
        median = find_median(points,1)
        leftP = None # points smaller or equal to median y
        rightP = None  # points greater than median y

    vertex = Vertex(points[median],build_kdtree(leftP,depth+1),build_kdtree(rightP,depth+1))

    # build_kdtree(leftP,depth+1),
    # build_kdtree(rightP,depth+1)
    # make vertex with median as root and leftP and rightP as children
    return None # return vertex