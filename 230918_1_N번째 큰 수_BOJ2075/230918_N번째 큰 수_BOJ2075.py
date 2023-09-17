# N번째 큰 수_BOJ2075

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                            # 행렬의 크기를 input 받고
lst = []                                    # 큰 수를 저장할 리스트를 생성하고
for i in range(N):                          # N개의 행을 반복해서
    A = list(map(int, input().split()))     # 한 행을 리스트로 input 받고
    for a in A:                             # 행을 반복해서
        if len(lst) < N:                    # 저장할 리스트의 길이가 N보다 작다면
            heapq.heappush(lst, a)          # lst에 a를 heappush한다
        else:                               # 저장할 리스트의 길이가 N과 같거나 크다면
            if lst[0] < a:                  # lst에 가장 작은 수가 a보다 작다면
                heapq.heappop(lst)          # lst에서 제일 작은수를 heappop하고
                heapq.heappush(lst, a)      # lst에 a를 heappush한다
print(lst[0])                               # N번째 큰 숫자를 출력한다