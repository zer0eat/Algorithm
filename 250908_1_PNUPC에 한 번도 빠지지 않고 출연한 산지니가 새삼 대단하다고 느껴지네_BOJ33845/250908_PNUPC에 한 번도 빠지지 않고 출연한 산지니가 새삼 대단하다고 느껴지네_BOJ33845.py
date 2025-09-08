# PNUPC에 한 번도 빠지지 않고 출연한 산지니가 새삼 대단하다고 느껴지네_BOJ33845

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = input().strip() # 아이디를 input받고
T = input().strip() # 문자를 input받고
ans = ''            # 정답을 저장할 변수를 생성해서
for t in T:         # 문자를 반복해서
    if t not in S:  # 해당 문자가 아이디에 포함되지 않다면
        ans += t    # 정답에 문자를 추가한다
print(ans)          # 아이디에 포함되지 않은 문자만 출력한다