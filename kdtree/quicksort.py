# algorytm sortujący quicksort potrzebny do znajdowania mediany
# w algorytmie kdtree

import numpy as np
eps = 1e-10

# wersja Lomuto
def partition_lomuto(arr,l,r,dim):
    pivot = arr[r][dim]
    i = l-1
    for j in range(l,r):
        if arr[j][dim] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1

# wersja Hoare'a
def partition_hoare(arr,l,r,dim):
    pivot = arr[l][dim]
    i = l-1
    j = r+1
    while True:
        i+=1
        while arr[i][dim] < pivot:
            i+=1
        j-=1
        while arr[j][dim] > pivot:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j] = arr[j],arr[i]

def partition_hoare_np(arr, l, r, dim):
    pivot = arr[l, dim]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while arr[i, dim] < pivot:
            i += 1
        j -= 1
        while arr[j, dim] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j].copy(), arr[i].copy()

def quicksort_np(arr, l, r, dim):
    if l < r:
        q = partition_hoare_np(arr, l, r, dim)
        quicksort_np(arr, l, q, dim)
        quicksort_np(arr, q + 1, r, dim)


def quicksort(arr,l,r,dim):
    if l<r:
        q = partition_hoare(arr,l,r,dim)
        quicksort(arr,l,q,dim)
        quicksort(arr,q+1,r,dim)


# test = [(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)]
# quicksort(test,0,len(test)-1,1)
# print(test)
# test_np = np.array(test)
# print(test_np)
# quicksort_np(test_np, 0, len(test_np) - 1, 1)
# print(test_np)
