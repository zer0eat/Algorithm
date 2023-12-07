# 게리멘더링2_BOJ17779

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 시의 크기를 input 받고
people = [list(map(int, input().split())) for _ in range(N)]    # 시의 인구수를 input 받는다
ans = 1e9                                                       # 인구가 가장 많은 선거구와 가장 적은 선거구의 차이를 저장할 변수를 생성하고

def find(d1,d2,x,y):
    global ans                                                  # 정답을 저장할 변수를 global로 선언하고
    g1, g2, g3, g4, g5 = 0, 0, 0, 0, 0                          # 1번부터 5번 선거구까지 인구수를 저장할 변수를 생성한다
    for i in range(N):                                          # 행을 반복하고
        for j in range(N):                                      # 열을 반복해서
            if 0<=i<x+d1 and 0<=j<=y:                           # 행이 x+d1보다 작고 열이 y와 같거나 작을 때
                if 0<=i<x:                                      # 행이 꼭지점보다 작다면
                    g1 += people[i][j]                          # 1구역에 인구수를 저장하고
                else:                                           # 행이 꼭지점과 같거나 클 때
                    if 0<=j<y-(i-x):                            # 열이 경계선보다 작다면
                        g1 += people[i][j]                      # 1구역에 인구수를 저장하고
                    else:                                       # 열이 경계선에 걸치거나 크다면
                        g5 += people[i][j]                      # 5구역에 인구수를 저장한다
            elif 0<=i<=x+d2 and y<j<N:                          # 행이 x+d2와 같거나 작고 열이 y보다 크고 N보다 작을 때
                if 0<=i<x:                                      # 행이 꼭지점보다 작다면
                    g2 += people[i][j]                          # 2구역에 인구수를 저장하고
                else:                                           # 행이 꼭지점과 같거나 클 때
                    if y+(i-x)<j<N:                             # 열이 경계선보다 크다면
                        g2 += people[i][j]                      # 2구역에 인구수를 저장하고
                    else:                                       # 열이 경계선에 걸치거나 작다면
                        g5 += people[i][j]                      # 5구역에 인구수를 저장한다
            elif x+d1<=i<N and 0<=j<y-d1+d2:                    # 행이 x+d1과 같거나 크고 N보다 작으며, 열이 y-d1+d2보다 작을 때
                if x+d1+d2<i<N:                                 # 행이 아래 꼭지점보다 크다면
                    g3 += people[i][j]                          # 3구역에 인구수를 저장하고
                else:                                           # 행이 꼭지점과 같거나 작을 때
                    if 0<=j<(y-d1)+(i-x-d1):                    # 열이 경계선보다 작다면
                        g3 += people[i][j]                      # 3구역에 인구수를 저장하고
                    else:                                       # 열이 경계선에 걸치거나 크다면
                        g5 += people[i][j]                      # 5구역에 인구수를 저장한다
            else:                                               # 이외의 구역에
                if x+d1+d2<i<N:                                 # 행이 아래 꼭지점보다 크다면
                    g4 += people[i][j]                          # 4구역에 인구수를 저장하고
                else:                                           # 행이 꼭지점과 같거나 작을 때
                    if (y+d2)-(i-x-d2)<j<N:                     # 열이 경계선보다 크다면
                        g4 += people[i][j]                      # 4구역에 인구수를 저장하고
                    else:                                       # 열이 경계선에 걸치거나 작다면
                        g5 += people[i][j]                      # 5구역에 인구수를 저장한다
    else:                                                       # 모든 구역을 5개의 선거구에 편입했다면
        lst = [g1,g2,g3,g4,g5]                                  # 선거구의 인구수를 리스트에 저장하고
        ans = min(ans, max(lst)-min(lst))                       # 현재 가장 큰 선거구와 가장 작은 선거구의 차이와 ans 중 더 작은 값을 ans에 저장한다

for d1 in range(1, N):                                          # 경계의 길이 d1을 1부터 N-1까지 반복하고
    for d2 in range(1, N):                                      # 경계의 길이 d2를 1부터 N-1까지 반복해서
        for x in range(N):                                      # 경계선의 위쪽 꼭지점 x를 N만큼 반복해서
            if x+d1+d2<N:                                       # 경계선의 가장 아래 지점이 N보다 작을 때
                for y in range(N):                              # 경계선의 위쪽 꼭지점 y를 N만큼 반복해서
                    if 0<=y-d1 and y+d2<N:                      # 경계선의 왼쪽이 0이상이고 경계선의 오른쪽이 N보다 작다면
                        find(d1,d2,x,y)                         # x,y의 꼭지점에서 d1,d2의 경계선으로 이루어진 선거구의 인구수를 find함수를 통해 계산한다
print(ans)                                                      # 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 출력한다