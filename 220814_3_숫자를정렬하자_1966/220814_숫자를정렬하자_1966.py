# 숫자를 정렬하자_1966

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N = int(input()) # 입력할 숫자 수
    arr = list(map(int, input().split()))
    # 버블정렬로 작은 수부터 정렬
    for a in range(N-1, 0, -1):
        for b in range(a):
            if arr[b] > arr[b + 1]:
                arr[b], arr[b + 1] = arr[b + 1], arr[b]
    print(f'#{t+1}', *arr)
