# 퇴사_BOJ14501

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 상담할 수 있는 날짜를 input 받고
TP = [list(map(int, input().split())) for _ in range(N)]    # 상담기간과 수익을 리스트로 input 받는다
ans = 0                                                     # 정답을 저장할 변수를 생성한다

def recur(start, tmp):
    global ans                                              # ans를 global 변수로 선언하고
    ans = max(ans, tmp)                                     # ans와 tmp 중 더 큰 값을 저장한다
    if start >= N:                                          # start가 N 이상이라면
        return                                              # return한다
    for i in range(start, N):                               # start부터 N까지 반복해서
        if i+TP[i][0] <= N:                                 # i일 부터 퇴사 전에 상담이 끝난다면
            tmp += TP[i][1]                                 # 수익을 tmp에 더하고
            recur(i+TP[i][0], tmp)                          # i+TP[i][0]일부터 상담을 탐색하고
            tmp -= TP[i][1]                                 # 수익을 tmp에서 빼준다

recur(0, 0)                                                 # 0번째부터 상담을 탐색한다
print(ans)                                                  # 얻을 수 있는 최대 이익을 출력한다