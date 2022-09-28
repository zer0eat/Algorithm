# 그룹나누기_14280_시간초과

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    team = []
    for m in range(M):
        a = set([arr[2*m], arr[2*m + 1]])
        flag = False

        for e in range(len(team)):
            for b in a:
                if b in team[e]:
                    team[e] = team[e]|a
                    flag = True
                    break
            if flag == True:
                break
        else:
            team.append(a)

    for e2 in range(len(team)-1, -1, -1):
        for e3 in range(e2):
            # print(e2, e3, team)
            if len(team[e2])+len(team[e3]) > len(team[e2]|team[e3]):
                team[e3] = team[e2]|team[e3]
                team.pop(e2)

    for am in team:
        N -= len(am)
    else:
        print(f'#{t+1}', N + len(team))

