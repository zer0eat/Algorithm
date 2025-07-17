# 다면체_BOJ10569

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input받고
for t in range(T):                      # 테스트 케이스를 반복해서
    V, E = map(int, input().split())    # 꼭지점의 수와 모서리의 수를 input받고
    print(2 + E - V)                    # 면의 수를 출력한다