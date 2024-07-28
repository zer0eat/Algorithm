# MBTI_BOJ25640

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
jinho = input().strip()             # 진호의 MBTI를 input 받고
N = int(input())                    # 진호의 친구의 수를 input 받고
ans = 0                             # 정답을 저장할 변수를 생성한다
for n in range(N):                  # 진호의 친구를 반복해서
    if jinho == input().strip():    # 진호와 MBTI가 같다면
        ans += 1                    # 정답을 1 추가한다
print(ans)                          # 진호와 MBTI가 같은 친구의 수를 출력한다