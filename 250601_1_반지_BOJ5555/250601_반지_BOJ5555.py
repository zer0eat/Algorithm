# 반지_BOJ5555

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
B = input().strip()         # 문자를 input받고
N = int(input())            # 반지의 개수를 input받는다
ans = 0                     # 정답을 저장할 변수르 생성하고
for n in range(N):          # 반지의 수를 반복해서
    A = input().strip()     # 반지를 input받고
    if B in A+A:            # 문자가 반지안에 있다면
        ans += 1            # 개수를 1추가한다
print(ans)                  # 문자가 포함된 반지의 수를 출력한다