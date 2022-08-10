# selection_sort

arr = [7, 2, 5, 3, 4, 6]
N = len(arr)

for n in range(N):
    minidx = n # n을 최소값의 인덱스로 가정
    for i in range(n+1, N): # 최소값 인덱스 찾기
        if arr[minidx] > arr[i]:
            minidx = i
    arr[minidx], arr[n] = arr[n], arr[minidx]

print(arr)