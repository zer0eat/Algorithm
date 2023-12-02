# 맥주 마시면서 걸어가기_BOJ9205

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
T = int(input())                                                # 테스트케이스를 input 받고
for t in range(T):                                              # 테스트케이스를 반복해서
    N = int(input())                                            # 편의점의 개수를 input 받고
    s, e = map(int, input().split())                            # 집의 x,y 좌표를 input 받은 후
    store = []                                                  # 편의점의 위치를 저장할 리스트를 생성하고
    for n in range(N):                                          # 편의점의 수를 반복해서
        store.append(list(map(int, input().split())))           # 편의점의 좌표를 input받아 리스트에 append한 후
    festival = list(map(int, input().split()))                  # 페스티벌의 좌표를 input 받는다
    visited = [0]*N                                             # 편의점 방문표시를 할 리스트를 생성하고
    tmp = deque([[s,e]])                                        # 집의 좌표를 넣은 deque를 생성한다
    while tmp:                                                  # tmp가 빌때까지 반복해서
        x, y = tmp.popleft()                                    # tmp에서 x,y좌표를 꺼낸 후
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:     # 해당좌표에서 페스티벌까지 맨하탄 거리가 1000이하라면
            print('happy')                                      # 축제에 갈 수 있으므로 happy를 출력하고
            break                                               # while문을 종료한다
        for n in range(N):                                      # 편의점의 수를 반복해서
            if visited[n] == 0:                                 # 방문하지 않은 편의점이라면
                r, c = store[n]                                 # 편의점의 좌표를 저장하고
                if abs(x-r) + abs(y-c) <= 1000:                 # 현재위치에서 편의점까지 맨하탄 거리 1000이하라면
                    visited[n] = 1                              # 방문할 수 있으므로 방문표시하고
                    tmp.append([r,c])                           # tmp에 편의점 좌표를 append한다
    else:                                                       # tmp가 빌때까지 페스티벌에 도착하지 못했다면
        print('sad')                                            # sad를 출력한다