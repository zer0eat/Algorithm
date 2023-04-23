# Tangled in Cables_BOJ4763

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
total = float(input())                      # 가지고 있는 케이블의 길이를 저장하고
N = int(input())                            # 연결할 집 수를 input 받는다

name = dict()                               # 집 이름을 저장할 딕셔너리 생성
for _ in range(N):                          # 집 수를 반복해서
    name[input().strip()] = 0               # 집 이름을 key value를 0으로 저장한다

cable = dict()                              # 두 집 사이의 거리를 저장할 딕셔너리를 생성하고
M = int(input())                            # 두 집 사이의 거리를 input 받는다
for _ in range(M):                          # 두 집 사이의 거리의 수를 반복해서
    a, b, c = input().split()               # a, b에 집이름 c에 거리를 input 받고
    if cable.get(a) == None:                # a가 key인 원소가 없을 때
        cable[a] = [[float(c), b]]          # a가 key [[거리, 이어진 집]] value로 원소를 생성한다
    else:                                   # a가 key인 원소가 있을 때
        cable[a].append([float(c), b])      # a가 key인 value에 [거리, 이어진 집]을 append
    if cable.get(b) == None:                # b가 key인 원소가 없을 때
        cable[b] = [[float(c), a]]          # b가 key [[거리, 이어진 집]] value로 원소를 생성한다
    else:                                   # b가 key인 원소가 있을 때
        cable[b].append([float(c), a])      # b가 key인 value에 [거리, 이어진 집]을 append

tmp = [[0, list(name.keys())[0]]]           # tmp에 최소 스패닝 트리의 시작점[cost, 이어질 집]을 넣고 리스트를 생성
ans = 0                                     # 최소로 필요한 cable의 길이를 저장할 변수 생성
while tmp:                                  # tmp가 빌 때까지 반복해서
    cost, people = heapq.heappop(tmp)       # tmp에서 heappop해서 비용와 이어질 집을 변수에 저장하고
    if name.get(people) == 0:               # 이어질 집이 아직 방문 전이라면
        name[people] = 1                    # 방문표시를 하고
        ans += cost                         # ans에 비용을 더한다
        for r in cable.get(people):         # 이어질 집과 이어진 집을 반복해서
            if name.get(r[1]) == 0:         # 이어진 집이 방문 전이라면
                heapq.heappush(tmp, r)      # tmp에 heappush한다

if ans <= total:                            # 필요한 케이블의 길이가 total 이하라면
    ans = round(ans, 1)                     # 소수점 첫번째까지 반올림해서 저장하고
    print(f'Need {ans} miles of cable')     # 필요한 케이블을 출력한다
else:                                       # total보다 필요한 케이블이 길다면
    print('Not enough cable')               # 충분하지 않다는 메세지를 출력한다