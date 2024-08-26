# 줄줄이 박수_BOJ29718

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # 축제 행사장의 행과 열을 input 받고
baksu = [list(map(int, input().split())) for _ in range(N)] # 박수 친 횟수를 리스트로 input 받는다
sum_baksu = []                      # 열의 박수의 합을 저장할 리스트를 생성하고
for m in range(M):                  # 열을 반복하고
    tmp = 0                         # 박수의 합을 저장할 변수를 생성해서
    for n in range(N):              # 행을 반복해서
        tmp += baksu[n][m]          # m열의 박수의 수를 더한다
    else:                           # 모든 행을 반복했다면
        sum_baksu.append(tmp)       # 한 열의 박수의 수를 append한다
ans = 0                             # 정답을 저장할 변수를 생성하고
A = int(input())                    # A개의 열의 개수를 input 받고
for m in range(M-A+1):              # A개의 열씩 묶을 때 시작 열을 반복해서
    tmp = 0                         # A개의 열의 박수의 수를 저장할 변수를 생성하고
    for a in range(A):              # A개의 열을 반복해서
        tmp += sum_baksu[m+a]       # m부터 A개의 열을 더해준다
    else:                           # A개의 열을 모두 더했다면
        ans = max(ans, tmp)         # ans와 tmp 중 박수 수가 더 많은 수를 저장하고
print(ans)                          # 가장 많이 친 박수를 출력한다