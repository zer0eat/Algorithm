# 캠프 준비_BOJ16938

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, L, R, X = map(int, input().split())  # N 문제의수 / L 난이도의 최소합 / R 난이도의 최대합 / X 난이도의 차를 inpur받고
A = list(map(int, input().split()))     # 문제의 난이도를 리스트로 input 받는다
ans = 0                                 # 정답을 저장할 변수를 생성하고

def recur(Q, start):
    global ans                          # ans를 global 변수로 선언하고
    if sum(Q) > R:                      # 문제의 합이 R 초과라면
        return                          # return한다
    else:                               # 문제의 합이 R 이하라면
        if L <= sum(Q) <= R and len(Q) >= 2 and max(Q) - min(Q) >= X:   # 캠프에 사용할 조건이 맞은 경우엔
            ans += 1                    # ans를 1 추가하고
        for a in range(start, N):       # start문제부터 끝까지 반복해서
            Q.append(A[a])              # 해당 문제를 리스트에 담고
            recur(Q, a+1)               # recur함수로 문제조합을 탐색한 후
            Q.pop()                     # 넣었던 문제를 pop한다

recur([], 0)                            # recur함수로 문제조합을 탐색한 후
print(ans)                              # 캠프에 사용할 문제를 고르는 방법의 수를 출력한다