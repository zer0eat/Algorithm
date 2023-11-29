# 호텔_BOJ1106

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
C, N = map(int, input().split())                # C 늘리려는 사람의 수 / N 홍보할 도시의 수를 input 받고
dp = [1e9]*(C+101)                              # 사람을 늘릴때 마다 드는 비용을 저장할 리스트를 생성한다
dp[0] = 0                                       # 0명을 늘릴 때 0원이 든다고 저장하고
for i in range(N):                              # 홍보할 도시의 수를 반복해서
    cost, people = map(int, input().split())    # 홍보 비용과 비용당 늘어나는 인원을 input 받고
    for i in range(people, C+101):              # 늘어나는 인원수부터 비용을 저장하는 리스트 끝까지 반복해서
        dp[i] = min(dp[i-people]+cost, dp[i])   # i명의 사람을 늘리기 위해 드는 비용을 현재 저장된 비용과 people명 적은 비용에서 cost를 더한 비용중 작은 값으로 갱신한다
print(min(dp[C:]))                              # C이상의 값중 최소값을 출력해서 최소비용을 구한다