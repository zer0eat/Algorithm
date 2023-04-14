# 평범한배낭_BOJ12865

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())                                        # N 물건의 개수 / K 가방에 넣을 수 있는 무게
bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]                 # 가방 리스트의 행을 N+1개 열을 K+1개로 생성하여 각각의 인덱스가 N, K가 되게한다

for i in range(1, N+1):                                                 # 물건의 수를 반복하고
    W, V = map(int, input().split())                                    # i번째 물건 정보를 W 무게 / V 가치를 저장한다
    for j in range(1, K+1):                                             # 넣을 수 있는 무게를 반복해서
        if j < W:                                                       # 가방에 넣을 수 있는 무게(j)가 물건무게(W)보다 작다면
            bag[i][j] = bag[i-1][j]                                     # i번째 물건을 넣을 수 없으므로 현재까지 j무게에 가장 많이 넣을 수 있었던 윗줄의 j 원소의 값을 저장한다
        else:                                                           # 가방에 넣을 수 있는 무게(j)가 물건무게(W)보다 같거나 크다면
            bag[i][j] = max(V + bag[i - 1][j - W], bag[i - 1][j])       # i번째 물건을 넣을 수 있으므로 (i번째 물건과 그 무게를 뺀 무게 중 최대 가치(윗줄의 j-W 원소)를 더한 값 / 더하지 않고 이전 j무게에 가장 많이 넣을 수 있었던 윗줄의 j 원소)을 비교하여 더 큰값으로 저장한다
print(bag[N][K])                                                        # 마지막 행 마지막 열에 적힌 가치가 가장 크므로 해당 수치를 출력한다