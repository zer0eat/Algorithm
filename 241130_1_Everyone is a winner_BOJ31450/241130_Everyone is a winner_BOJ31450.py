# Everyone is a winner_BOJ31450

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
M, K = map(int, input().split())    # 메달의 수와 사람의 수를 input 받고
if M % K:                           # 모든 사람에게 같은 메달을 줄 수 없으면
    print('No')                     # No를 출력하고
else:                               # 모든 사람에게 같은 메달을 줄 수 있으면
    print('Yes')                    # Yes를 출력한다