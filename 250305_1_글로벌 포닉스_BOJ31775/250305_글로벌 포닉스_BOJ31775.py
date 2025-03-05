# 글로벌 포닉스_BOJ31775

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = [input().strip() for _ in range(3)] # 단어를 input 받고
ans = [0]*3                             # 정답을 저장할 리스트를 생성해서
for s in S:                             # 단어를 반복해서
    if s[0] == 'l':                     # 첫번째가 l이라면
        ans[0] = 1                      # 리스트의 첫번째에 저장하고
    elif s[0] == 'k':                   # 첫번째가 k라면
        ans[1] = 1                      # 리스트의 두번째에 저장하고
    elif s[0] == 'p':                   # 첫번째가 p라면
        ans[2] = 1                      # 리스트의 세번째에 저장하고
if sum(ans) == 3:                       # 모든 글자가 나왔다면
    print('GLOBAL')                     # 글로벌을 출력하고
else:                                   # 나이라면
    print('PONIX')                      # 포닉스를 출력한다