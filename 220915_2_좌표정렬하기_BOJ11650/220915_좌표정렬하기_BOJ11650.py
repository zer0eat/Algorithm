# 좌표정렬하기_BOJ11650

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())
arr = []
for n in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 버블 솔트
for i in range(N-1):
    for j in range(N-i-1):
        if arr[j][0] > arr[j + 1][0]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        elif arr[j][0] == arr[j + 1][0]:
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for a in arr:
    print(*a)


