# 방어율 무시 계산하기_BOJ25756

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 물약의 개수를 input 받고
W = list(map(int, input().split()))         # 물약을 리스트로 input 받아서
ans = 0                                     # 정답을 저장할 변수를 생성하고고
for n in range(N):                          # 물약의 수를 반복해서
    ans = 100-(100-(ans))*(100-(W[n]))/100  # 방어력 무시 능력치를 계산해서
    print(ans)                              # 정답을 출력한다