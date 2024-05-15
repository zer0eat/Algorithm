# 오각형, 오각형, 오각형…_BOJ1964.py

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 오각형의 개수를 input 받고
ans = 5                         # 정답을 저장할 변수를 생성해서
if N == 1:                      # 오각형의 개수가 1개라면
    print(ans)                  # 5개를 출력한다
else:                           # 오각형의 개수가 2이상이라면
    for n in range(3, N+2):     # 늘어나는 한변의 길이를 반복해서
        ans += 3*n-2            # 늘어나는 점을 정답에 더하고
        ans %= 45678            # 45678로 나눈 나머지만 저장한다
    print(ans % 45678)          # 정답을 45678로 나눈 나머지를 출력한다