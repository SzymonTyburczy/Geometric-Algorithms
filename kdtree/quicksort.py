# algorytm sortujący quicksort potrzebny do znajdowania mediany
# w algorytmie kdtree

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
    pivot = arr[(l+r)//2][dim]
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

def quicksort(arr,l,r,dim):
    if l<r:
        q = partition_hoare(arr,l,r,dim)
        quicksort(arr,l,q-1,dim)
        quicksort(arr,q+1,r,dim)

test = [(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)]
quicksort(test,0,len(test)-1,1)
print(test)