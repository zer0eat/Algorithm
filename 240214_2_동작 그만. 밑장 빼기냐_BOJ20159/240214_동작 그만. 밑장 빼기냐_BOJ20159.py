# 동작 그만. 밑장 빼기냐_BOJ20159

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                        # 카드의 개수를 input 받고
X = list(map(int, input().split()))                     # 카드의 값을 리스트로 input 받는다
p1 = [0]*(N//2)                                         # 홀수번째 카드의 합을 저장할 리스트를 생성하고
p2 = [0]*(N//2)                                         # 짝수번째 카드의 합을 저장할 리스트를 생성한다
for x in range(N):                                      # 카드를 반복해서
    if x%2:                                             # 홀수번째 카드라면
        p2[x//2] = p2[x//2-1] + X[x]                    # p2리스트에 누적합을 저장하고
    else:                                               # 짝수번째 카드라면
        p1[x//2] = p1[x//2-1] + X[x]                    # p1리스트에 누적합을 저장한다
ans = 0                                                 # 정훈이가 얻을 수 있는 최대 점수를 저장할 변수를 생성하고
for n in range(N//2):                                   # 홀수번째 카드를 반복해서
    ans = max(ans, p1[n] + p2[-1] - p2[n])              # ans와 마지막 카드를 정훈이가 받을 때 점수 중 큰 점수를 저장한다
ans2 = p1[-1]                                           # 상대방이 얻을 수 있는 최소 점수를 저장할 변수를 생성하고
for n in range(N//2-1):                                 # 짝수번째 카드를 반복해서
    if n == 0:                                          # 첫번째 카드라면
        ans2 = min(ans2, p1[-1] - p1[n] + X[-1])        # ans2와 맨 처음에 마지막 카드를 상대방이 받았을 때 점수 중 작은 점수를 저장한다
    ans2 = min(ans2, p2[n] + p1[-1] - p1[n+1] + X[-1])  # ans2와 마지막 카드를 상대방이 받았을 때 점수 중 작은 점수를 저장한다
print(max(ans, sum(X)-ans2))                            # ans와 전체점수에서 ans2만큼 뺀 값 중 더 큰 값을 출력한다