# 공 넣기_BOJ10810

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 바구니와 M 던지려는 공을 input 받고
basket = [0] * N                        # 바구니를 리스트로 생성한다
for _ in range(M):                      # 공을 던지는 횟수를 반복해서
    i, j, k = map(int, input().split()) # 바구니의 번호i,j 공의 번호 k를 input 받고
    for n in range(i-1, j):             # 바구니의 번호를 반복해서
        basket[n] = k                   # 바구니에 k를 저장한다
print(*basket)                          # 바구니에 있는 공을 출력한다