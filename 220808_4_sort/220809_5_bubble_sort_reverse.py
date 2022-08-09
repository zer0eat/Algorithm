def Bubblesort_reverse(a, N): #a=정렬할 리스트 N=원소수
    for i in range(0, N-1):
        for j in range(N-1, i ,-1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

print(Bubblesort_reverse([7, 8, 9, 6, 1, 4, 5, 2, 3], 9))