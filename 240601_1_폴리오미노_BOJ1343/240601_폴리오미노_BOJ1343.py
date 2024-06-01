# 폴리오미노_BOJ1343

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = list(input().strip().split('.'))    # 보드판을 input 받고
ans = ''                                # 정답을 저장할 변수를 생성한다
for a in A:                             # 보드판을 반복해서
    if len(a) % 2 == 0:                 # 보드판의 X가 짝수라면
        ans += 'AAAA'*(len(a)//4)       # AAAA로 덮을 수 있는 최대를 덮고
        ans += 'BB'*((len(a)%4)//2)     # BB로 덮을 수 있는 나머지를 덮은 후
        ans += '.'                      # .을 넣어 보드판을 채운다
    else:                               # 보드판의 X가 홀수라면
        print(-1)                       # 덮을 수 없으므로 -1을 출력하고
        quit()                          # 종료한다
print(ans[:-1])                         # 사전순으로 가장 앞서는 답을 출력한다