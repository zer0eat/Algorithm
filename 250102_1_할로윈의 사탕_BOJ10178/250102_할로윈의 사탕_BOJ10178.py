# 할로윈의 사탕_BOJ10178

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 테스트 케이스를 input 받고
for n in range(N):                      # 테스트 케이스를 반복해서
    c, v = map(int, input().split())    # 사탕과 형제의 수를 input 받고
    print(f'You get {c//v} piece(s) and your dad gets {c%v} piece(s).') # 정답을 출력한다