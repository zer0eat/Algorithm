# Rust Study_BOJ30033

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                                 # 정답을 저장할 변수를 생성하고
N = int(input())                        # 공부한 일수를 input 받고
lst = list(map(int, input().split()))   # 계획한 페이지를 input 받고
lst2 = list(map(int, input().split()))  # 공부한 페이지를 input 받고
for i in range(N):                      # 공부한 일수를 반복해서
    if lst[i] <= lst2[i]:               # 공부한 페이지가 더 많다면
        ans += 1                        # 정답에 추가하고
print(ans)                              # 계획보다 더 공부한 횟수를 출력한다