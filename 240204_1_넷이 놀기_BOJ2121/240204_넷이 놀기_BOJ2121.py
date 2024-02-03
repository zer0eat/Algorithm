# 넷이 놀기_BOJ2121

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                                        # 점의 개수를 input 받고
r, c = map(int, input().split())                                                        # r 가로 길이 / c 세로길이를 input 받는다
dot = set(tuple(map(int, input().split())) for _ in range(N))                           # 점들을 input 받아 set에 저장하고
ans = 0                                                                                 # 정답을 저장할 변수를 생성한다
for x, y in dot:                                                                        # 점들을 반복해서
    if ((x+r, y) in dot) and ((x, y+c) in dot) and ((x+r, y+c) in dot):                 # x,y점으로 직사각형을 만들 때 점들이 있다면
        ans += 1                                                                        # 정답을 1 추가한다
print(ans)                                                                              # 가능한 경우의 수를 출력한다