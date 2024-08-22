# 가계부(Easy)_BOJ12836

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, Q = map(int, input().split())        # 살아온 날 / 쿼리의 개수를 input 받고
M = [0]*(N+1)                           # 살아온 날만큼 리스트를 생성한다
for q in range(Q):                      # 쿼리를 반복해서
    a, b, c = map(int, input().split()) # 쿼리를 input 받고
    if a == 1:                          # 1번 쿼리라면
        for n in range(b, N+1):         # b부터 살아온날까지 반복해서
            M[n] += c                   # 변화한 금액을 정산한다
    else:                               # 2번 쿼리라면
        print(M[c] - M[b-1])            # b, c까지 돈의 변화량을 출력한다