# 퀵정렬_14221

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def quick(A):                               
    if len(A) == 0:                         # 길이가 0이 되면 A를 return한다
        return A
    pivot = A[0]                            # 맨 왼쪽 값을 pivot으로 잡고
    i = 1                                   # i가 인덱스의 1부터
    j = len(A) - 1                          # j는 리스트의 맨 오른쪽으로 놓고 시작한다
    while j >= i:                           # j가 i보다 작아질때 까지 반복하며
        if A[j] > pivot:                    # A[j]가 pivot보다 크면 
            j -= 1                          # 왼쪽으로 한칸 이동한다
        elif A[i] <= pivot:                 # A[i]가 pivot보다 작거나 같으면  
            i += 1                          # 오른쪽으로 한칸 이동한다
        else:                               # A[i]가 pivot보다 크고 A[j]가 pivot보다 작을 때
            A[i], A[j] = A[j], A[i]         # A[i]와 A[j]를 바꿔준 후
            i += 1                          # i를 오른쪽으로
            j -= 1                          # j를 왼쪽으로 이동시킨다
    else:                                   # j가 i보다 작아졌다면
        A[0], A[j] = A[j], A[0]             # pivot을 A[j]와 바꾼다
        A[:j] = quick(A[:j])                # 피봇의 좌측을 잘라 quicksort 하고
        A[j+1:] = quick(A[j+1:])            # 피봇의 우측을 잘라 quicksort 한다
        return A

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):                          # 테스트 케이스를 반복할 때
    N = int(input())                        # 정렬할 정수의 개수
    A = list(map(int, input().split()))     # A에 N개의 정수를 리스트로 받음
    quick(A)                                # quicksort 진행
    print(f'#{t+1}', A[N//2])


