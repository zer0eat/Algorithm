# 다각형의대각선_BOJ3049

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 다각형의 꼭지점의 수
print(N*(N-1)*(N-2)*(N-3)//24)      # 4개의 꼭지점마다 교차점이 1개씩 나오므로 nC4로 교점의 개수를 출력