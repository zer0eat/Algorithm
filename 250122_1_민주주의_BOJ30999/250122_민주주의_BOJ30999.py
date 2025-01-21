# 민주주의_BOJ30999

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # 출제문제의 수와 심사위원의 수를 input 받고
ans = 0                             # 정답을 저장할 변수를 생성한다
for n in range(N):                  # 문제의 수를 반복해서
    Q = list(input().strip())       # 심사결과를 input 받고
    tmp = 0                         # 심사위원의 점수를 저장할 변수를 생성한다
    for q in Q:                     # 심사결과를 반복해서
        if q == 'O':                # 통과라면
            tmp += 1                # 점수를 1 추가한다
    if tmp > (M//2):                # 과반수 이상의 동의를 얻었다면
        ans += 1                    # 문제를 통과시킨다
print(ans)                          # 통과된 문제의 수를 출력한다