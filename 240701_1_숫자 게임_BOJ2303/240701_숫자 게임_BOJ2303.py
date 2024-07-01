# 숫자 게임_BOJ2303

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations

# input 받기
N = int(input())                        # 사람의 수를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성하고
cnt = 0                                 # 일의 자리의 합을 저장할 변수를 생성한다
for n in range(1, N+1):                 # 사람의 수를 반복해서
    A = list(map(int, input().split())) # 카드 5장을 리스트로 input 받고
    for a in combinations(A, 3):        # 카드의 3장씩 조합해서
        b = sum(a)%10                   # 3장의 합의 일의 자리를 구하고
        if b >= cnt:                    # 3장의 합의 일의 자리가 cnt보다 같거나 크다면
           ans = n                      # ans에 번호를 저장하고
           cnt = b                      # cnt에 가장 큰 일의 자리의 합을 저장한다
print(ans)                              # 카드 3장의 합의 일의 자리가 가장 큰 사람을 출력한다