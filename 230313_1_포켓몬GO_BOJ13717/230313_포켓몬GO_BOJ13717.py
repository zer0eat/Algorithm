# 포켓몬GO_BOJ13717

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # N 포켓몬 종류의 수
ans = 0                                 # 진화시킬 수 있는 포켓몬을 저장할 변수 생성
maxtmp = 0                              # 가장 많이 진화시킨 포켓몬의 수를 저장할 변수 생성
ansPoketmon = ''                        # 가장 많이 진화시킨 포켓몬의 이름을 저장할 변수 생성

for n in range(N):                      # 포켓몬의 종류의 수만큼 반복해서
    poketmon = input().strip()          # 포켓몬의 이름을 input 받고
    k, m = map(int, input().split())    # k 진화할 때 필요한 포켓몬 사탕의 수 / m 가지고 있는 포켓몬 사탕의 수
    tmp = 0                             # 해당 포켓몬이 진화한 횟수를 저장할 변수를 생성
    while k <= m:                       # 진화에 필요한 사탕보다 남은 사탕이 더 많다면 반복해서
        m -= k                          # 남은 사탕에서 진화 필요한 사탕의 수를 빼고
        m += 2                          # 남은 사탕에 돌려 받은 사탕 2개를 추가한다
        ans += 1                        # 총 진화한 횟수를 1 추가하고
        tmp += 1                        # 현재 포켓몬의 진화한 횟수를 1 추가한다
    else:                               # 진화에 필요한 사탕보다 남은 사탕이 적다면
        if maxtmp < tmp:                # 가장 많이 진화시킨 포켓몬의 수가 현재 포켓몬의 진화수보다 작다면
            maxtmp = tmp                # 가장 많이 진화시킨 포켓몬의 수를 현재 포켓몬의 수로 저장하고
            ansPoketmon = poketmon      # 가장 많이 진회시킨 포켓몬의 이름을 현재 포켓몬의 이름으로 저장한다
else:                                   # 모든 포켓몬을 반복했다면
    print(ans)                          # 진화한 포켓몬 수를 출력하고
    print(ansPoketmon)                  # 가장 많이 진화한 포켓몬 이름을 출력한다