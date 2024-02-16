# 미술가 미미_BOJ20950

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 물감의 개수를 input 받고
color = [list(map(int, input().split())) for _ in range(N)] # 물감의 색을 리스트로 input 받는다
gom = list(map(int, input().split()))                       # 곰두리색 물감을 input 받고
ans = 1e9                                                   # 정답을 저장할 변수를 생성한다

def recur(dep, start, mun):
    global ans, N                                           # global 변수로 선언하고
    if dep > 1:                                             # dep이 2 이상이라면
        tmp = [0, 0, 0]                                     # 색상을 혼합할 리스트를 생성하고
        for m in mun:                                       # mun에 저장한 색을 반복해서
            tmp[0] += m[0]                                  # R색을 tmp[0]에 더해주고
            tmp[1] += m[1]                                  # G색을 tmp[1]에 더해주고
            tmp[2] += m[2]                                  # B색을 tmp[2]에 더해주고
        else:                                               # 모든 색을 더했다면
            tmp[0] //= len(mun)                             # R색을 물감의 수로 나눠주고
            tmp[1] //= len(mun)                             # G색을 물감의 수로 나눠주고
            tmp[2] //= len(mun)                             # B색을 물감의 수로 나눠주고
            diff = abs(gom[0] - tmp[0]) + abs(gom[1] - tmp[1]) + abs(gom[2] - tmp[2])   # 문두리색과 곰두리색의 차이를 저장한다
        ans = min(ans, diff)                                # 곰두리색과 차이가 가장 적은 값을 ans에 저장한다
    if dep == 7 or dep == N:                                # dep이 7이거나 N이라면
        return                                              # 더 이상 색을 섞을 수 없으므로 return한다
    for i in range(start, N):                               # start부터 물감을 반복해서
        mun.append(color[i])                                # i번째 색을 append하고
        recur(dep+1, i+1, mun)                              # 깊이를 dep+1, i+1번째 색부터 탐색해서 곰두리색과 가장 가까운 색을 찾고
        mun.pop()                                           # i번재 색을 pop한다

recur(0, 0, [])                                             # 깊이를 0, 0번째 색부터 탐색해서 곰두리색과 가장 가까운 색을 찾는다
print(ans)                                                  # 곰두리색과 문두리색의 차이를 출력한다