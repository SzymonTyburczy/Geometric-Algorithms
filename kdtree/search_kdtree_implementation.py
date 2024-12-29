#implementacja wyszukiwania w kdtree

from quicksort import quicksort
from build_kdtree_implementation_2 import Vertex,divide_points,sort_by_dim

# area = [x1,y1,x2,y2]
# root = Vertex
def point_in_area(point,area):
    if point[0] >= area[0] and point[0] <= area[2] and point[1] >= area[1] and point[1] <= area[3]:
        return True
    return False

# zostaje do implementacji
def search_kdtree(root,area,result):
    if root.left == None and root.right == None:
        if point_in_area(root.point,area):
            result.append(root.point)
        # if lewe poddrzewo zawiera sie cale w obszarze:
        # dodaj cale lewe poddrzewo do result
        # elif lewe poddrzewo przecina sie z obszarem:
        # search_kdtree(root.left,area,result)
        # if prawe poddrzewo zawiera sie cale w obszarze:
        # dodaj cale prawe poddrzewo do result
        # elif prawe poddrzewo przecina sie z obszarem:
        # search_kdtree(root.right,area,result)