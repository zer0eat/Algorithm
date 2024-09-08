# 크냑과 3D 프린터_BOJ30923

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 프린트 할 길이를 input 받고
stick = list(map(int, input().split())) # 막대의 길이를 리스트로 input 받는다
ans = stick[0]*4 + 2                    # 첫번째 막대를 출력하기 위한 겉넓이를 변수로 저장하고
for n in range(1, N):                   # 두번째부터 N번째까지 반복해서
    ans += stick[n]*3 + 2               # 맞 닿아 있는 면을 뺀 n번째 기둥의 겉넓이를 저장하고
    if stick[n-1] < stick[n]:           # n번째 기둥이 전보다 크다면
        ans += stick[n]                 # 겹치지 않는 곳의 넓이를 더하고
        ans -= 2*stick[n-1]             # 겹치는 곳의 넓이를 제거한다
    else:                               # n번째 기둥이 전보다 작다면
        ans -= stick[n]                 # 겹치는 곳의 넓이를 제거한다
print(ans)                              # 필요한 겉넓이를 출력한다