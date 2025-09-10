# 겨울왕국 티켓 예매_BOJ18247

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input받고
for t in range(T):                      # 테스트 케이스를 반복해서
    N, M = map(int, input().split())    # 행과 열을 input받고
    if N < 12 or M < 4:                 # l4가 없다면
        print(-1)                       # -1을 출력하고
    else:                               # l4가 있다면
        print(11 * M + 4)               # 찾아가는 횟수를 출력한다