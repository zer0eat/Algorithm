# 홈방범서비스_2117

# input.txt
import sys
sys.stdin = open('input.txt')

# input 열기
T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스를 반복할 때
    N, M = map(int, input().split())                                # N = 도시의 크기 / M = 하나의 집이 지불하는 비용
    jido = [list(map(int, input().split())) for _ in range(N)]      # 도시의 지도를 행렬 형태로 받음

    cnt = 0                                                         # 도시 전체에서 집이 있는 곳을 세기 위한 변수
    for i in range(N):                                              # 도시의 행을 반복하고
        for j in range(N):                                          # 도시의 열을 반복할 때
            if jido[i][j] == 1:                                     # 만약 집이 있는 곳이라면
                cnt += 1                                            # cnt에 1을 추가한다
    else:                                                           # 반복이 끝났다면
        maxi = cnt * M                                              # maxi에 지도 전체에서 낼 수 있는 최대 비용을 저장한다

    K = 1                                                           # 방범 범위를 나타낼 변수 K를 설정하고
    ans = 0                                                         # 손해 보지 않는 선에서 '방범 범위 내에 집이 가장 많이 있을 때' 저장할 변수를 생성
    while K * K + (K - 1) * (K - 1) <= maxi:                        # 'maxi = 지도 전체의 최대 비용' 보다 '방범 범위의 비용이 작을 때'만 반복한다
        for i in range(N):                                          # 방범 범위의 중심을 행을 반복하고
            for j in range(N):                                      # 열을 반복하면서 탐색한다
                tmp = 0                                             # 방범 범위 내 집의 개수를 저장할 변수를 생성하고
                for k in range(-K+1, K):                            # jido[i][j]를 중심으로 위 아래로 K 범위를 반복하고
                    for q in range(-K+1 + abs(k), K - abs(k)):      # jido[i][j]를 중심으로 왼쪽 오른쪽으로 K 범위를 반복할 때
                        if 0 <= i + k < N and 0 <= j + q < N:       # 지도 내에 범위에서만
                            if jido[i + k][j + q] == 1:             # 집이 있다면
                                tmp += 1                            # tmp에 집을 하나 추가한다
                else:                                               # K 범위 내 탐색이 끝났을 때
                    if (tmp * M) - (K * K + (K - 1) * (K - 1)) >= 0:    # 손해가 아니라면
                        if ans < tmp:                               # ans에 저장된 최대 가구수와 현재 가구수를 비교해서 현재 범위 내 가구수가 많다면
                            ans = tmp                               # ans를 현재 범위 내 가구수로 변경한다
        else:                                                       # K 범위의 모든 방범 구역을 탐색 했다면
            K += 1                                                  # K를 하나 증가시킨다
    print(f'#{t+1}', ans)                                           # 최대 가구수를 출력한다