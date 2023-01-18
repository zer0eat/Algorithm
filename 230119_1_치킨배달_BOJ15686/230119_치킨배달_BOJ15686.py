# 치킨배달_BOJ15686

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def case(n):
    global M                                    # M을 global로 불러와서
    if n == len(chicken):                       # n이 치킨집의 수가 되어 모든 치킨집의 비트를 살펴보았다면
        if sum(bit) == M:                       # bit의 합이 M이 될때
            tmp.append(bit[:])                  # tmp에 bit를 append하고
        return                                  # 리턴한다
    bit[n] = 1                                  # n번째 비트를 1로 만들고
    case(n+1)                                   # 다음 비트의 탐색으로 넘어가고
    bit[n] = 0                                  # n번째 비트를 0으로 돌린 후
    case(n+1)                                   # 다음 비트의 탐색으로 넘어간다

# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 지도의 행렬의 길이 / M 남길 치킨집의 개수
jido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 집과 치킨집이 있는 지도를 input 받아 jido에 저장

house = []                                      # 집의 좌표를 저장할 빈 리스트 생성
chicken = []                                    # 치킨집의 좌표를 저장할 빈 리스트 생성

for i in range(N):                              # 행을 반복하고
    for j in range(N):                          # 열을 반복해서
        if jido[i][j] == 1:                     # 해당 좌표가 1이라면 집이므로
            house.append([i, j])                # house에 append 하고
        elif jido[i][j] == 2:                   # 해당 좌표가 2라면 치킨집이므로
            chicken.append([i, j])              # chicken에 append 한다

tmp = []                                        # M개의 치킨집을 고를 경우의 수를 저장할 빈리스트 생성
bit = [0] * len(chicken)                        # bit에 치킨집의 개수만큼 0을 요소를 만들어 리스트를 생성하고
case(0)                                         # case 함수를 돌려 경우의 수를 찾는다

ans = 10000                                     # 정답을 저장할 변수를 생성하고
for pick in tmp:                                # M개의 치킨집을 고른 경우의 수를 반복해서
    tmp2 = []                                   # 고른 치킨집의 좌표를 저장할 빈 리스트를 만들고
    for p in range(len(pick)):                  # M개의 치킨집을 고른 경우의 수 중 한개를 반복해서
        if pick[p] == 1:                        # bit가 1이라 선택한 치킨집이 나왔다면
            tmp2.append(chicken[p])             # tmp2에 선택한 치킨집의 좌표를 append한다
    else:                                       # 치킨집을 고른 경우의 수 중 한개의 반복을 마쳤다면
        money = 0                               # pick의 경우에 드는 비용을 저장할 변수를 생성하고
        for h in house:                         # 집의 좌표를 반복해서
            moneyTmp = 100                      # 집과 치킨집의 최소 비용을 저장할 변수를 생성하고
            for m in tmp2:                      # 치킨집의 좌표를 반복해서
                A = abs(h[0]-m[0]) + abs(h[1]-m[1])                     # 집과 치킨집의 거리 비용을 A에 저장해서
                if A < moneyTmp:                # 최소비용보다 A가 작다면
                    moneyTmp = A                # A를 최소비용으로 바꿔준다
            else:                               # 모든 치킨집과 비교를 마쳤다면
                money += moneyTmp               # money에 해당 집의 최소 비용을 더해준다
        else:                                   # 모든 집의 비용의 탐색을 마쳤다면
            if money < ans:                     # 현재 저장된 최소 비용보다 money가 더 적게 든다면
                ans = money                     # money를 최소비용으로 저장해준다
else:                                           # 모든 경우의 수 탐색을 마쳤다면
    print(ans)                                  # 최소비용을 출력한다