# 최소이동거리_14283

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                # 테스트 케이스
for t in range(T):                                              # 테스트 케이스를 반복할 때
    N, E = map(int, input().split())                            # N 노드의 개수 / E 간선의 수

    A = [list(map(int, input().split())) for e in range(E)]     # 간선의 정보를 A에 행렬 형태로 저장
    cost = [0] * (N + 1)                                        # 해당 노드까지 가는 비용을 저장할 빈리스트 생성

    for a in A:                                                 # 간선을 하나씩 반복할 때
        if cost[a[1]]:                                          # 비용이 등록된 상태라면
            if cost[a[1]] > cost[a[0]] + a[2]:                  # 등록된 비용보다 현재 입력된 비용이 작다면
                cost[a[1]] = cost[a[0]] + a[2]                  # 비용을 더 낮은 비용으로 바꿔준다
        else:                                                   # 아직 비용이 등록되지 않았다면
            cost[a[1]] = cost[a[0]] + a[2]                      # 노드의 번호를 인덱스로 사용해서 해당 노드까지의 비용을 저장한다
    print(f'#{t+1}', cost[-1])