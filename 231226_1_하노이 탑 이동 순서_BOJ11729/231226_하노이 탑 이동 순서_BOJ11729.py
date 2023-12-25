# 하노이 탑 이동 순서_BOJ11729

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
K = int(input())                            # 원판의 개수를 input 받고

def hanoi(N, start, target, assistant):
    if N == 1:                              # 이동하는 원판이 1번 원판인 경우
        print(start, target)                # 시작에서 도착으로 경로를 출력하고
        return                              # return한다
    hanoi(N-1, start, assistant, target)    # 이동하는 원판을 하나 줄이고 시작에서 보조로 이동하도록 탐색한다
    print(start, target)                    # 시작에서 도착으로 경로를 출력하고
    hanoi(N-1, assistant, target, start)    # 이동하는 원판을 하나 줄이고 보조에서 도착으로 이동하도록 탐색한다

print(2**K-1)                               # 이동 횟수를 출력한 후
hanoi(K, 1, 3, 2)                           # hanoi를 통해 이동경로를 탐색한다