# 치킨댄스를 추는 곰곰이를 본 임스_BOJ25191

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 치킨의 수를 input 받고
A, B = map(int, input().split())    # 콜라와 맥주의 수를 input 받아서
print(min(N, A//2 + B))             # 먹을 수 있는 치킨의 수를 출력한다