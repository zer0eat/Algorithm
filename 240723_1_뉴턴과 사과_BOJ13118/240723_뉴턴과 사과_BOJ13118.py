# 뉴턴과 사과_BOJ13118

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
P = list(map(int, input().split())) # 사람이 서있는 위치를 input 받고
x, y, r = map(int, input().split()) # 사과의 x, y 위치 r 반지름을 input 받고
for p in range(4):                  # 4명의 사람을 반복해서
    if P[p] == x:                   # 사과와 부딪히는 위치에 있다면
        print(p+1)                  # 사람의 순번을 출력하고
        break                       # for문을 break한다
else:                               # 부딪히는 사람이 없다면
    print(0)                        # 0을 출력한다