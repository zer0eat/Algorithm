# SciComLove (2025)_BOJ33810

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                 # 정답을 저장할 변수를 생성하고
A = 'SciComLove'        # 원래 문자를 저장하고
S = input().strip()     # 바뀐 문자를 input받고
for n in range(10):     # 문자를 반복해서
    if A[n] != S[n]:    # 문자가 바뀌었다면
        ans += 1        # 정답에 개수를 추가하고
print(ans)              # 바뀐 문자의 수를 출력한다