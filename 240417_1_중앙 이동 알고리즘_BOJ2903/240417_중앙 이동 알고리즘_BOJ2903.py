# 중앙 이동 알고리즘_BOJ2903

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 점을 찍을 횟수를 input 받고
ans = 2             # 한변에 있는 점의 개수를
for n in range(N):  # 점을 찍을 횟수를 반복해서
    ans += ans-1    # 한변에 늘어난 점의 개수를 더해준다
print(ans**2)       # 한변에 있는 점만큼 가로 줄이 있으므로 제곱값으로 모든 점의 수를 출력한다