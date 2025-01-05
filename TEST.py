import GENERATE
from random import randint
from timeit import default_timer as timer
import QuadTree as QUADT
import kdtree_object_implementation_leafs as KdBuild
import sys
sys.setrecursionlimit(10000000)


def testout():
    for i in range(200, 1001, 200):
        test = GENERATE.generate_points(i, 1000)
        Kd = KdBuild.KDtree(test)
        QT = QUADT.CreateQuad(test)

        v = 300
        while True:
            x1 = randint(-v, v)
            x2 = randint(-v, v)
            y1 = randint(-v, v)
            y2 = randint(-v, v)

            s1 = Kd.search_area(((x1, y1), (x2, y2)), Kd.get_root(), 0)
            s2 = QT.query(x1, y1, x2, y2)

            if set(s1) != set(s2):
                print("ERROR!")
                print(test)
                break
            print("OK")
            break

testout()




# TEST 1
print("TEST 1")
one = GENERATE.try1_1()
start = timer()
Kd = KdBuild.KDtree(one)
s1 = Kd.search_area(((0, 0), (100, 150)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(one)
s2 = QT.query(0, 0, 100, 150)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 2
print("TEST 2")
two = GENERATE.try2_2()
start = timer()
Kd = KdBuild.KDtree(two)
s1 = Kd.search_area(((0, 0), (70, 60)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(two)
s2 = QT.query(0, 0, 70, 60)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 3
print("TEST 3")
three = GENERATE.try3_3()
start = timer()
Kd = KdBuild.KDtree(three)
s1 = Kd.search_area(((-10, 0), (50, 70)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(three)
s2 = QT.query(-10, 0, 50, 70)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")



# TEST 4
print("TEST 4")
four = GENERATE.try4_4()
start = timer()
Kd = KdBuild.KDtree(four)
s1 = Kd.search_area(((0, 0), (10, 15)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(four)
s2 = QT.query(0, 0, 10, 15)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 5
print("TEST 5")
five = GENERATE.try5_5()
start = timer()
Kd = KdBuild.KDtree(five)
s1 = Kd.search_area(((-5, 0), (10, 2)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(five)
s2 = QT.query(-5, 0, 10, 2)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 6
print("TEST 6")
six = GENERATE.try_evenly1_6()
start = timer()
Kd = KdBuild.KDtree(six)
s1 = Kd.search_area(((0, 0), (8, 8)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(six)
s2 = QT.query(0, 0, 8, 8)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 7
print("TEST 7")
seven = GENERATE.try_evenly2_7()
start = timer()
Kd = KdBuild.KDtree(seven)
s1 = Kd.search_area(((0, 0), (7, 7)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(seven)
s2 = QT.query(0, 0, 7, 7)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 8
print("TEST 8")
eight = GENERATE.try_evenly3_8()
start = timer()
Kd = KdBuild.KDtree(eight)
s1 = Kd.search_area(((-200, -200), (500, 500)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(eight)
s2 = QT.query(-200, -200, 500, 500)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 9
print("TEST 9")
nine = GENERATE.try_evenly4_9()
start = timer()
Kd = KdBuild.KDtree(nine)
s1 = Kd.search_area(((-4, -4), (4, 4)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(nine)
s2 = QT.query(-4, -4, 4, 4)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 10
print("TEST 10")
ten = GENERATE.try_evenly5_10()
start = timer()
Kd = KdBuild.KDtree(ten)
s1 = Kd.search_area(((-2, -2), (2, 2)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(ten)
s2 = QT.query(-2, -2, 2, 2)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 11
print("TEST 11")

start = timer()
Kd = KdBuild.KDtree(GENERATE.try_halfevenly6_11())
s1 = Kd.search_area(((4, 4), (10, 10)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(GENERATE.try_halfevenly6_11())
s2 = QT.query(4, 4, 10, 10)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")

# TEST 12
print("TEST 12")

start = timer()
Kd = KdBuild.KDtree(GENERATE.try_halfevenly7_12())
s1 = Kd.search_area(((-10, 0), (10, 15)), Kd.get_root(), 0)
end = timer()


start1 = timer()
QT = QUADT.CreateQuad(GENERATE.try_halfevenly7_12())
s2 = QT.query(-10, 0, 10, 15)
end1 = timer()

if set(s1) != set(s2):
    print("ERROR!")
    print(set(s1))
    print(set(s2))
else:
    print("OK")

print(f"Czas wykonania KDTree: {end - start} sekund, Czas wykonania QuadTree: {end1 - start1} sekund")
