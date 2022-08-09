def Bubblesort(a, N): #a=정렬할 리스트 N=원소수
    for i in range(N-1, 0 ,-1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
    return a

print(Bubblesort([7, 8, 9, 6, 1, 4, 5, 2, 3], 9))
