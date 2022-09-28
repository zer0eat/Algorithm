# 최소생산비용_14225

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 순열
def f(n):
    global cost                                                 # 비용을 저장할 변수를 불러오고
    tmp = 0                                                     # 임시로 비용을 저장할 변수를 생성한 뒤
    for a in range(n):                                          # n번째 제품까지 결정했을 때 n까지 반복해서
        tmp += arr[a][pp[a]]                                    # tmp에 a번 제품의 a번 공장에서 생산 비용을 저장하고
        if tmp > cost:                                          # 만약 cost 보다 커지면
            return                                              # return해서 가지치기를 한다

    if n == N:                                                  # 모든 공장을 확정 했을 때
        if cost > tmp:                                          # cost가 tmp보다 크다면
            cost = tmp                                          # cost에 tmp를 저장해준다

    for a in range(n, N):                                       # n부터 N까지 반복해서
        pp[a], pp[n] = pp[n], pp[a]                             # a번째 요소와 n번째 요소를 바꿔준 후
        f(n+1)                                                  # 다음 순열로 들어간다
        pp[a], pp[n] = pp[n], pp[a]                             # 바꿔준 요소를 제자리로 돌린다

# input 받기
T = int(input())                                                # 테스트 케이스
for t in range(T):                                              # 테스트 케이스를 반복할 때
    N = int(input())                                            # 제품의 수
    arr = [list(map(int, input().split())) for _ in range(N)]   # 제품별 공장의 생산비를 행렬형태로 저장

    pp = [i for i in range(N)]                                  # 공장의 인덱스를 저장하는 리스트 생성

    cost = 99*N                                                 # 최소비용을 저장할 변수를 생성하고
    f(0)                                                        # 순열을 돌려 한공장에서 한 제품씩 생산할 수 있는 조건을 찾는다

    print(f'#{t+1}', cost)