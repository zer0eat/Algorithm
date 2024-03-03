# 게임_BOJ1072

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X, Y = map(int, input().split())    # X 게임 횟수 / Y 이긴 게임을 input 받고
Z = int((Y*100)/X)                  # 승률을 저장한다
l = 1                               # 승률이 바뀌기 위해 이겨야할 최소 승수를 변수로 만들고
r = X                               # 승률이 바뀌기 위해 이겨야할 최대 승수를 변수로 만든다
ans = 0                             # 정답을 저장할 변수를 생성하고
while l <= r:                       # l이 r과 같아질때까지 반복해서
    mid = (l+r)//2                  # l,r의 중점을 저장하고
    xx = X+mid                      # 게임횟수를 xx에 저장하고
    yy = Y+mid                      # 이긴게임을 yy에 저장해서
    zz = int((yy*100)/xx)           # zz에 승률을 저장한 뒤
    if Z == zz:                     # 승률이 바뀌지 않았다면
        l = mid+1                   # l을 mid+1로 바꿔주고
    else:                           # 승률이 바뀌었다면
        ans = mid                   # 이겨야할 최소승수를 ans에 저장하고
        r = mid-1                   # r을 mid-1로 바꿔준다
if ans == 0:                        # ans가 0이라면
    print(-1)                       # 승률이 바뀌지 않으므로 -1을 출력하고
else:                               # ans가 0이 아니라면
    print(ans)                      # 승률이 바뀌는 최소 승수를 출력한다