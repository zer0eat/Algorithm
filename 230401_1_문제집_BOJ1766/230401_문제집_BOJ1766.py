# 문제집_BOJ1766

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())        # N 문제의수 / M 문제정보의 수
order = dict()                          # 문제 순서를 저장할 딕셔너리 생성
inDegree = [0]*(N+1)                    # 문제 순서를 저장할 리스트 생성
for _ in range(M):                      # 문제정보의 수를 반복해서
    a, b = map(int, input().split())    # 먼저풀 문제를 a, 나중에풀 문제를 b에 input 받고
    if order.get(a) == None:            # a가 key인 딕셔너리가 아직 없다면
        order[a] = [b]                  # a가 key인 딕셔너리에 value를 [b]로 생성한 후
        inDegree[b] += 1                # b의 inDegree를 1 추가한다
    else:                               # 만약 이미 a가 key인 딕셔너리가 존재한다면
        order[a].append(b)              # a가 key인 딕셔너리에 b를 append하고
        inDegree[b] += 1                # b의 inDegree를 1 추가한다

tmp = []                                # 풀 문제를 임시로 담아 놓은 리스트를 생성하고
for i in range(1, N+1):                 # 1번 문제부터 N번 문제까지 반복해서
    if inDegree[i] == 0:                # 만약 i번째 문제의 inDegree 값이 0이라서 우선적으로 풀 문제라면
        heapq.heappush(tmp, i)          # tmp에 i문제를 heappush한다

ans = []                                # 문제를 풀 순서를 저장할 리스트를 생성하고
while tmp:                              # tmp가 빌때까지 반복해서
    a = heapq.heappop(tmp)              # tmp에서 heappop해서 a에 저장한 후
    ans.append(a)                       # ans에 a를 append 한다
    if order.get(a) != None:            # a가 key인 딕셔너리가 존재한다면
        for b in order[a]:              # a가 key인 딕셔너리의 value에 담긴 문제를 반복해서
            inDegree[b] -= 1            # 해당 문제의 inDegree를 -1씩 감소시키고
            if inDegree[b] == 0:        # 감소시킨후 inDegree가 0이 되었다면
                heapq.heappush(tmp, b)  # tmp에 b를 heappush한다
print(*ans)                             # tmp가 모두 빌때까지 반복했다면 ans를 출력한다
