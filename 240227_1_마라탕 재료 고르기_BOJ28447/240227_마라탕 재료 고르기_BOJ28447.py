# 마라탕 재료 고르기_BOJ28447

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())                        # N 마라탕 재료의 수 / K 고를 재료의 수를 input 받고
C = [list(map(int, input().split())) for _ in range(N)] # 궁합을 나타내는 수열을 리스트로 input 받는다
ans = -100000                                           # 정답을 저장할 변수를 생성한다

def recur(dep, start, taste):
    global ans                                          # ans를 global 변수로 선언하고
    if dep == K:                                        # K개의 재료를 골랐다면
        tmp = 0                                         # 궁합을 저장할 변수를 생성하고
        for t1 in range(K-1):                           # 재료를 반복하고
            for t2 in range(t1+1, K):                   # t1 재료와 궁합을 볼 다른 재료를 반복해서
                tmp += C[taste[t1]][taste[t2]]          # 두 재료의 궁합을 tmp에 더한다
        ans = max(ans, tmp)                             # ans와 tmp 중 더 큰 값의 궁합을 저장하고
        return                                          # return한다
    for i in range(start, N):                           # start 재료부터 반복해서
        taste.append(i)                                 # i번째 재료를 넣고
        recur(dep+1, i+1, taste)                        # 깊이 dep+1, i+1번째 재료부터 궁합을 탐색하고
        taste.pop()                                     # i번째 재료를 pop한다

if K == 1:                                              # 재료의 수가 1이라면
    print(0)                                            # 궁합을 낼 수 없으므로 0을 출력한다
else:                                                   # 재료의 수가 2이상이라면
    recur(0, 0, [])                                     # 깊이 0, 0번째 재료부터 궁합을 탐색한다
    print(ans)                                          # 마라탕 맛의 최댓값을 출력한다