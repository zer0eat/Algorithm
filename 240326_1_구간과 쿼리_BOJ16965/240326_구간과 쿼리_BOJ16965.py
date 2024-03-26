# 구간과 쿼리_BOJ16965

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                                    # 쿼리의 개수를 input 받고
dic = dict()                                        # 쿼리의 이동 경로를 저장할 딕셔너리를 생성하고
query = []                                          # 1번 쿼리를 저장할 리스트를 생성한다
for n in range(N):                                  # 쿼리의 개수를 반복해서
    num, a, b = map(int, input().split())           # num 쿼리의 종류 / a 시작 / b 끝을 input 받고
    if num == 1:                                    # 1번 쿼리라면
        dic[len(query)+1] = []                      # 쿼리의 이동 경로를 저장하기 위해 원소를 생성하고
        for q in range(len(query)):                 # 저장된 1번 쿼리를 반복해서
            if query[q][0] < a and a < query[q][1]: # 현재 쿼리에서 q+1번 쿼리로 이동할 수 있다면
                dic[len(query)+1].append(q+1)       # 현재 쿼리를 키로 도착지를 value에 append한다
            if query[q][0] < b and b < query[q][1]: # 현재 쿼리에서 q+1번 쿼리로 이동할 수 있다면
                dic[len(query)+1].append(q+1)       # 현재 쿼리를 키로 도착지를 value에 append한다
            if a < query[q][0] and query[q][0] < b: # q+1번 쿼리에서 현재 쿼리로 이동할 수 있다면
                dic[q+1].append(len(query)+1)       # q+1 쿼리를 키로 도착지를 value에 append한다
            if a < query[q][1] and query[q][1] < b: # q+1번 쿼리에서 현재 쿼리로 이동할 수 있다면
                dic[q+1].append(len(query)+1)       # q+1 쿼리를 키로 도착지를 value에 append한다
        query.append((a, b))                        # 현재 쿼리를 리스트에 append 한다
    else:                                           # 2번 쿼리라면
        visited = [0]*(N+1)                         # 방문표시를 할 리스트를 생성하고
        dq = deque([a])                             # 시작점을 넣은 deque를 생성하고
        flag = False                                # 도착지에 도착한 것을 표시할 변수를 생성한다
        while dq:                                   # dq가 빌때까지 반복해서
            A = dq.popleft()                        # dq에서 원소를 popleft해서
            visited[A] = 1                          # A를 방문표시하고
            for d in dic[A]:                        # A와 연결된 지점을 반복해서
                if d == b:                          # 도착지에 도달한다면
                    flag = True                     # flag를 True로 바꾸고
                    break                           # for문을 종료한다
                if visited[d] == 0:                 # 연결된 지점이 방문 전이라면
                    dq.append(d)                    # deque에 연결된 지점을 append한다
            if flag:                                # flag가 True라면
                print(1)                            # 도착지에 도착할 수 있으므로 1을 출력하고
                break                               # while문을 종료한다
        else:                                       # dq가 빌때까지 반복을 마쳤다면
            print(0)                                # 도착지에 도착할 수 없으므로 0을 출력한다