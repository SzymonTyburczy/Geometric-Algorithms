# generowanie danych testowych
import numpy as np
from kdtree_object_implementation_leafs import KDtree

def generate_random_uniform_points(n, low, high):
    points = []
    for i in range(n):
        points.append((np.random.uniform(low, high),np.random.uniform(low, high)))
    return points

def make_result(points,area):
    result = []
    for point in points:
        if area[0][0] <= point[0] <= area[1][0] and area[0][1] <= point[1] <= area[1][1]:
            result.append(point)
    return result

def check_result(result,expected):
    if len(result) != len(expected):
        return False
    for point in expected:
        if point not in result:
            return False
    return True
