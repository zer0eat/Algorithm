# 사과_BOJ10833

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 학교의 수를 input받고
ans = 0                             # 정답을 저장할 변수를 생성한다
for n in range(N):                  # 학교의 수를 반복해서
    s, a = map(int,input().split()) # 학생과 사과의 수를 input받고
    ans += a%s                      # 학생에게 사과를 똑같이 나눠주고 남은 사과를 변수에 더하고
print(ans)                          # 남은 사과의 수를 출력한다