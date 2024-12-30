#implementacja wyszukiwania w kdtree

from quicksort import quicksort
from build_kdtree_implementation_2 import Vertex,divide_points,sort_by_dim,kdtree_init

# area = [x1,y1,x2,y2]
# root = Vertex
def point_in_area(point,area):
    if area[0] <= point[0] <= area[2] and area[1] <= point[1] <= area[3]:
        return True
    return False

# zostaje do implementacji
# z box bounding
# def search_kdtree_bb(root,area,result,depth=0,bounds = (float("-inf"),float("-inf"),float("inf"),float("inf"))):
#     if root.left == None and root.right == None:
#         if point_in_area(root.point,area):
#             result.append(root.point)
        # if lewe poddrzewo zawiera sie cale w obszarze:
        # dodaj cale lewe poddrzewo do result
        # elif lewe poddrzewo przecina sie z obszarem:
        # search_kdtree_bb(root.left,area,result)
        # if prawe poddrzewo zawiera sie cale w obszarze:
        # dodaj cale prawe poddrzewo do result
        # elif prawe poddrzewo przecina sie z obszarem:
        # search_kdtree_bb(root.right,area,result)

# bez box bounding
def search_kdtree(root, area, result, depth=0):
    if root is None:
        return None
    # if root.left is None or root.right is None:
    #     if point_in_area(root.point, area):
    #         result.append(root.point)
    print(root.point,depth)

    if point_in_area(root.point, area):
        result.append(root.point)

    if depth % 2 == 0:
        if root.point[0] <= area[0]:
            search_kdtree(root.right, area, result, depth + 1)
        elif root.point[0] >= area[2]:
            search_kdtree(root.left, area, result, depth + 1)
        else:
            search_kdtree(root.left, area, result, depth + 1)
            search_kdtree(root.right, area, result, depth + 1)
    else:
        if root.point[1] <= area[1]:
            search_kdtree(root.right, area, result, depth + 1)
        elif root.point[1] >= area[3]:
            search_kdtree(root.left, area, result, depth + 1)
        else:
            search_kdtree(root.left, area, result, depth + 1)
            search_kdtree(root.right, area, result, depth + 1)
    return None

test_data = [(1,1),(1,4),(2,3),(6,2),(4,4),(2,7),(6,6),(8,4),(8,6)]
root = kdtree_init(test_data)
print(root.point,root.left,root.right) # (4, 4)
result = []
search_kdtree(root,(2,2,6,6),result)
print(result) # [(2, 3), (4, 4), (6, 2), (6, 6)]