# RGB거리_BOJ1149

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                                       # 집의 개수
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # N개의 줄에 각 집을 빨강, 초록, 파랑으로 색칠하는데 드는 비용 input받음

for i in range(1, N):                                                       # 1부터 N-1까지 반복해서
    house[i][0] = min(house[i - 1][1], house[i - 1][2]) + house[i][0]       # 인덱스가 i번인 집을 앞집(i-1)과 겹치지 않게 빨강으로 칠하는데 드는 가장 최소 비용으로 바꿔 저장
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + house[i][1]       # 인덱스가 i번인 집을 앞집(i-1)과 겹치지 않게 초록으로 칠하는데 드는 가장 최소 비용으로 바꿔 저장
    house[i][2] = min(house[i - 1][1], house[i - 1][0]) + house[i][2]       # 인덱스가 i번인 집을 앞집(i-1)과 겹치지 않게 파랑으로 칠하는데 드는 가장 최소 비용으로 바꿔 저장
else:                                                                       # 반복을 마쳤으면
    print(min(house[N-1]))                                                  # 모든 집을 칠하는 최소비용을 출력한다


