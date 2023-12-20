# 차이를 최대로_BOJ10819

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import permutations

# input 받기
N = int(input())                        # 배열의 길이를 input 받고
lst = list((map(int, input().split()))) # 배열의 원소를 리스트로 input 받는다
ans = 0                                 # 최댓값을 저장할 변수를 생성하고
for A in permutations(lst, N):          # 배열의 순열로 반복해서
    tmp = 0                             # 하나의 순열의 최대 차이를 저장할 변수를 생성하고
    for i in range(N-1):                # 배열의 길이를 반복해서
        tmp += abs(A[i] - A[i+1])       # i번째 원소에서 i+1번째 원소를 뺀 절대값을 tmp에 더한다
    else:                               # 모든 원소를 반복했다면
        ans = max(ans, tmp)             # ans에 ans와 tmp 중 더 큰 값을 저장하고
print(ans)                              # 차이의 최대값을 출력한다