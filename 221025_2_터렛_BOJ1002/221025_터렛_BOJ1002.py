# 터렛_BOJ1002

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                                                                   # 테스트 케이스
for t in range(T):                                                                              # 테스트 케이스를 반복해서
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())                             # 1번의 x,y 좌표와 2번의 x,y좌표 그리고 반지름의 길이를 받는다

    if x1 == x2 and y1 == y2 and r1 == r2:                                                      # 두 원의 중심과 반지름이 동일하다면
        print(-1)                                                                               # -1을 출력하고
    elif (y2-y1)**2 + (x2-x1)**2 == (r1 + r2)**2 or (y2-y1)**2 + (x2-x1)**2 == (r1 - r2)**2:    # 두 원이 한점에서 만난다면
        print(1)                                                                                # 1을 출력하고
    elif (r1 - r2)**2 < (y2-y1)**2 + (x2-x1)**2 < (r1 + r2)**2:                                 # 두 점에서 만난다면
        print(2)                                                                                # 2를 출력한다
    elif (y2-y1)**2 + (x2-x1)**2 < (r1 - r2)**2 or (y2-y1)**2 + (x2-x1)**2 > (r1 + r2)**2:      # 두 점이 만나지 않는 다면
        print(0)                                                                                # 0을 출력한다