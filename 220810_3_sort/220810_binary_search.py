# binary search
def binaryserach(a, N ,key)
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: #검색성공
            return true
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return  fakse #검색실패

# 재귀 함수 이용
def binarysearch2(a, low, high, key):
    if low > high: #검색실패
        return false
    else:
        middle = (low + high) // 2
        if key == a[middle]: #검색성공
            return true
        elif key < a[middle]:
            return binarysearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarysearch2(a, middle+1, high key)