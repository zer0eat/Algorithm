# 수박 게임_BOJ31868

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())    # 수박의 단계와 체리의 수를 input받고
ans = 2**(N-1)                      # 수박이 되기 위해 필요한 체리의 수를 구해서
print(K//ans)                       # 체리로 만들 수 있는 수박의 수를 출력한다