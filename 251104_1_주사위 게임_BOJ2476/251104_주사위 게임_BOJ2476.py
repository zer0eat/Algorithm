# 주사위 게임_BOJ2476

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 주사위의 수를 input받고
ans = 0                                     # 정답을 저장할 변수를 생성한다
for n in range(N):                          # 주사위의 수를 반복해서
    L = list(map(int, input().split()))     # 3개의 주사위의 숫자를 input받고
    if len(set(L)) == 1:                    # 세 주사위가 모두 같다면
        tmp = L[0]*1000+10000               # 상금을 저장하고
    elif len(set(L)) == 2:                  # 두 주사위가 같다면
        if L[0] == L[1] or L[0] == L[2]:    # 첫번째가 겹치는 수라면
            tmp = L[0]*100+1000             # 상금을 저장하고
        else:                               # 두번째가 겹치는 수라면
            tmp = L[1]*100+1000             # 상금을 저장하고
    else:                                   # 겹치지 않는다면
        tmp = max(L)*100                    # 상금을 저장하고
    ans = max(ans, tmp)                     # 가장 큰 상금을 저장해서
print(ans)                                  # 최대 상금을 출력한다