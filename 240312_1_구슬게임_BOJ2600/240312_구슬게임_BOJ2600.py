# 구슬게임_BOJ2600

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
b = list(map(int, input().split()))                 # 뺄 수 있는 구슬의 수를 리스트로 input 받고
dp = [[-1]*501 for _ in range(501)]                 # 승리를 저장할 dp를 생성한다

def game(k1, k2):
    if dp[k1][k2] >= 0:                             # k1, k2 구슬의 승부가 저장되어 있다면
        return dp[k1][k2]                           # 해당 값을 return한다
    for i in range(3):                              # 뺄 수 있는 구슬의 수를 반복해서
        if b[i] <= k1 and game(k1 - b[i], k2) == 0: # 1번 통의 구슬이 b[i]보다 작고 k1-b[i]와 k2의 승부 결과가 B가 이긴다면
            dp[k1][k2] = 1                          # k1, k2의 승부에 1을 저장하고
            return dp[k1][k2]                       # 1을 리턴한다
    for j in range(3):                              # 뺄 수 있는 구슬의 수를 반복해서
        if b[j] <= k2 and game(k1, k2 - b[j]) == 0: # 2번 통의 구슬이 b[i]보다 작고 k1-b[i]와 k2의 승부 결과가 B가 이긴다면
            dp[k1][k2] = 1                          # k1, k2의 승부에 1을 저장하고
            return dp[k1][k2]                       # 1을 리턴한다
    dp[k1][k2] = 0                                  # k1, k2의 승부에 0을 저장하고
    return dp[k1][k2]                               # 0을 리턴한다

for _ in range(5):                                  # 5번 구슬의 개수를 반복해서
    k1, k2 = map(int, input().split())              # 두 통의 구슬의 수를 input 받고
    if game(k1, k2):                                # 두 통의 구슬의 수를 통해 이기는 사람을 구할 때 1이 나오면
        print('A')                                  # A가 승리한다고 출력한다
    else:                                           # 두 통의 구슬의 수를 통해 이기는 사람을 구할 때 0이 나오면
        print('B')                                  # B가 승리한다고 출력한다