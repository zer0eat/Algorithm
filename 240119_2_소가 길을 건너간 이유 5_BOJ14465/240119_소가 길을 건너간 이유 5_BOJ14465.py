# 소가 길을 건너간 이유 5_BOJ14465

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K, B = map(int, input().split())         # N 횡단번호의 수 / K 신호등의 수 / B 고장난 신호등의 수를 input 받고
traffic = [1] * (N+1)                       # 신호등을 리스트에 저장한다
for b in range(B):                          # 고장난 신호등을 반복해서
    traffic[int(input())] = 0               # 고장난 신호등을 표시한다
ans = 0                                     # 고장나지 않은 신호등을 저장할 변수를 생성하고
tmp = sum(traffic[:K])                      # 0부터 K-1까지 고장나지 않은 신호등의 수를 저장한다
for i in range(N-K+1):                      # 신호등을 반복해서
    tmp = tmp - traffic[i] + traffic[i+K]   # 고장나지 않은 신호등의 합에 i번째 신호등을 빼고 i+K번째 신호등의 상태를 더해준 후
    ans = max(ans, tmp)                     # ans와 tmp 중 고장나지 않은 신호등이 더 많은 수를 ans에 저장한다
print(K-ans)                                # K개 중 정상작동하는 신호등의 수를 빼서 수리해야하는 최소 숫자를 출력한다