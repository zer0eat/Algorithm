# 사탕게임_BOJ3085

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 보드의 크기를 input 받고
candy = [list(input().strip()) for n in range(N)]               # 보드에 놓인 사탕을 input 받는다
d = [[0,1],[1,0]]                                               # 좌우 상하 사탕을 바꾸기 위한 리스트를 생성하고

def find1(i,j,r,c,candy):
    candy[r][c], candy[i][j] = candy[i][j], candy[r][c]         # 캔디의 위치를 바꾸고
    ctmp = 1                                                    # c 열의 행을 탐색하여 개수를 저장할 변수를 생성하고
    jtmp = 1                                                    # j 열의 행을 탐색하여 개수를 저장할 변수를 생성하고
    itmp = 1                                                    # i 행의 열을 탐색하여 개수를 저장할 변수를 생성하고
    maxN = 0                                                    # 최대 사탕의 개수를 저장할 변수를 생성한다
    cc = candy[0][c]                                            # c 열의 첫번째 사탕을 저장하고
    jj = candy[0][j]                                            # j 열의 첫번째 사탕을 저장하고
    ii = candy[i][0]                                            # i 행의 첫번째 사탕을 저장한다
    for q in range(1, N):                                       # 1부터 N까지 반복해서
        if cc == candy[q][c]:                                   # 저장된 사탕과 다음 사탕이 같은 종류라면
            ctmp += 1                                           # 개수를 하나 추가하고
        else:                                                   # 저장된 사탕과 다음 사탕이 다른 종류라면
            maxN = max(maxN, ctmp)                              # maxN에 현재 저장된 가장 많은 개수와 이때까지 먹을 수 있는 개수 중 더 큰 값을 저장하고
            cc = candy[q][c]                                    # 현재 사탕의 종류로 바꿔 저장하고
            ctmp = 1                                            # 먹을 수 있는 사탕의 수를 1로 초기화한다
        if jj == candy[q][j]:                                   # 저장된 사탕과 다음 사탕이 같은 종류라면
            jtmp += 1                                           # 개수를 하나 추가하고
        else:                                                   # 저장된 사탕과 다음 사탕이 다른 종류라면
            maxN = max(maxN, jtmp)                              # maxN에 현재 저장된 가장 많은 개수와 이때까지 먹을 수 있는 개수 중 더 큰 값을 저장하고
            jj = candy[q][j]                                    # 현재 사탕의 종류로 바꿔 저장하고
            jtmp = 1                                            # 먹을 수 있는 사탕의 수를 1로 초기화한다
        if ii == candy[i][q]:                                   # 저장된 사탕과 다음 사탕이 같은 종류라면
            itmp += 1                                           # 개수를 하나 추가하고
        else:                                                   # 저장된 사탕과 다음 사탕이 다른 종류라면
            maxN = max(maxN, itmp)                              # maxN에 현재 저장된 가장 많은 개수와 이때까지 먹을 수 있는 개수 중 더 큰 값을 저장하고
            ii = candy[i][q]                                    # 현재 사탕의 종류로 바꿔 저장하고
            itmp = 1                                            # 먹을 수 있는 사탕의 수를 1로 초기화한다
    else:                                                       # 반복을 마쳤다면
        candy[r][c], candy[i][j] = candy[i][j], candy[r][c]     # 캔디를 원상태로 돌려 놓은 후
        maxN = max(maxN, jtmp, itmp, ctmp)                      # maxN에 가장 많은 개수를 저장하고
    return maxN                                                 # maxN을 return한다

def find2(i,j,r,c,candy):
    candy[r][c], candy[i][j] = candy[i][j], candy[r][c]         # 캔디의 위치를 바꾸고
    rtmp = 1                                                    # r 행의 열을 탐색하여 개수를 저장할 변수를 생성하고
    itmp = 1                                                    # i 행의 열을 탐색하여 개수를 저장할 변수를 생성하고
    jtmp = 1                                                    # j 열의 행을 탐색하여 개수를 저장할 변수를 생성하고
    maxN = 0                                                    # 최대 사탕의 개수를 저장할 변수를 생성한다
    rr = candy[r][0]                                            # r 행의 첫번째 사탕을 저장하고
    ii = candy[i][0]                                            # i 행의 첫번째 사탕을 저장하고
    jj = candy[0][j]                                            # j 열의 첫번째 사탕을 저장한다
    for q in range(1, N):                                       # 1부터 N까지 반복해서
        if rr == candy[r][q]:                                   # 저장된 사탕과 다음 사탕이 같은 종류라면
            rtmp += 1                                           # 개수를 하나 추가하고
        else:                                                   # 저장된 사탕과 다음 사탕이 다른 종류라면
            maxN = max(maxN, rtmp)                              # maxN에 현재 저장된 가장 많은 개수와 이때까지 먹을 수 있는 개수 중 더 큰 값을 저장하고
            rr = candy[r][q]                                    # 현재 사탕의 종류로 바꿔 저장하고
            rtmp = 1                                            # 먹을 수 있는 사탕의 수를 1로 초기화한다
        if ii == candy[i][q]:                                   # 저장된 사탕과 다음 사탕이 같은 종류라면
            itmp += 1                                           # 개수를 하나 추가하고
        else:                                                   # 저장된 사탕과 다음 사탕이 다른 종류라면
            maxN = max(maxN, itmp)                              # maxN에 현재 저장된 가장 많은 개수와 이때까지 먹을 수 있는 개수 중 더 큰 값을 저장하고
            ii = candy[i][q]                                    # 현재 사탕의 종류로 바꿔 저장하고
            itmp = 1                                            # 먹을 수 있는 사탕의 수를 1로 초기화한다
        if jj == candy[q][j]:                                   # 저장된 사탕과 다음 사탕이 같은 종류라면
            jtmp += 1                                           # 개수를 하나 추가하고
        else:                                                   # 저장된 사탕과 다음 사탕이 다른 종류라면
            maxN = max(maxN, jtmp)                              # maxN에 현재 저장된 가장 많은 개수와 이때까지 먹을 수 있는 개수 중 더 큰 값을 저장하고
            jj = candy[q][j]                                    # 현재 사탕의 종류로 바꿔 저장하고
            jtmp = 1                                            # 먹을 수 있는 사탕의 수를 1로 초기화한다
    else:                                                       # 반복을 마쳤다면
        candy[r][c], candy[i][j] = candy[i][j], candy[r][c]     # 캔디를 원상태로 돌려 놓은 후
        maxN = max(maxN, jtmp, itmp, rtmp)                      # maxN에 가장 많은 개수를 저장하고
    return maxN                                                 # maxN을 return한다

ans = 0                                                         # 정답을 저장할 변수를 생성하고
for i in range(N):                                              # 행을 반복하고
    for j in range(N):                                          # 열을 반복해서
        for k in range(2):                                      # 좌우 상하 이동여부를 반복해서
            r = i + d[k][0]                                     # 이동한 곳의 행의 위치를 r에 저장하고
            c = j + d[k][1]                                     # 이동한 곳에 열의 위치를 c에 저장해서
            if 0<=r<N and 0<=c<N:                               # r과 c가 보드의 안에 위치한다면
                if k == 0:                                      # k가 0이면
                    ans = max(ans, find1(i,j,r,c,candy))        # 좌우로 바꾸고 최대 개수를 탐색해서 ans에 저장하고
                else:                                           # k가 1이면
                    ans = max(ans, find2(i,j,r,c,candy))        # 상하로 바꾸고 최대 개수를 탐색해서 ans에 저장한다
print(ans)                                                      # ans에 저장된 사탕의 최대 개수를 출력한다