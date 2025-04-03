# 백발백준하는 명사수_BOJ22938

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
x1, y1, r1 = map(int, input().split())      # 원의 중심과 반지름을 input 받고
x2, y2, r2 = map(int, input().split())      # 다른 원의 중심과 반지름을 input 받고
if (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2:    # 겹치는 부분이 있다면
    print('YES')                            # YES를 출력하고
else:                                       # 겹치는 부분이 없다면
    print('NO')                             # NO를 출력한다