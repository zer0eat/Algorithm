# 재수강_BOJ31822

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
c = input().strip()[:5]         # 재수강할 과목을 input 받고
N = int(input())                # 과목의 수를 input 받고
ans = 0                         # 정답을 저장할 변수를 생성해서
for n in range(N):              # 과목의 수를 반복해서
    tmp = input().strip()[:5]   # 과목을 input 받고
    if c == tmp:                # 재수강할 수 있다면
        ans += 1                # 정답의 수를 추가하고
print(ans)                      # 재수강 가능한 과목을 출력한다