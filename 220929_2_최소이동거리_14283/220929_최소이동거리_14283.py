# 최소이동거리_14283

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def find(a):
    global cost, tmp                            # cost와 tmp를 불러오고
    if a == N:                                  # 도착지까지 도착했을 경우에
        if cost <= tmp:                         # cost보다 tmp가 크다면 return해서 넘어간다
            return
        else:                                   # cost보다 tmp가 작다면
            cost = tmp                          # cost를 tmp로 갱신해주고 return
        return
    for A in ch1[a]:                            # a에서 출발했을 때 도착지의 정보를 반복해서
        tmp += A[1]                             # 도착지까지의 cost를 tmp에 더했을 때
        if tmp <= cost:                         # tmp가 cost보다 작다면
            find(A[0])                          # 도착지를 출발점으로 잡고 다시 find 함수를 돌린다
        tmp -= A[1]                             # tmp에 더했던 cost를 다시 빼주어 원래 값으로 돌려준다 

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복할 때
    N, E = map(int, input().split())            # N 0번부터 시작했을 때 끝지점의 수 / E 도로의 개수

    ch1 = [[] for _ in range(N+1)]              # 인덱스를 출발점으로 했을 때 도착지와 cost를 저장할 리스트

    for e in range(E):                          # 도로의 수만큼 반복할 때
        A = list(map(int, input().split()))     # A에 리스트 형태로 도로의 정보를 받고
        ch1[A[0]].append([A[1], A[2]])          # ch1의 리스트의 인덱스 A[0]에 [A[1], A[2]]를 append

    tmp = 0                                     # 중간 중간의 지점을 저장하는 변수
    cost = 1000000000                           # 0부터 N까지 길이의 최소
    find(0)                                     # find 함수를 돌린다
    print(f'#{t+1}', cost)                      # 최저 비용을 출력한다