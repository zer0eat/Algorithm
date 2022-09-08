# 하키_BOJ1358

# input.txt
import sys
sys.stdin = open('input.txt')
import math

# input 받기
W, H, X, Y, P = map(int, input().split())
# P = 선수의 수 / W = 너비 / H = 높이 및 원의 지름 / X, Y = 가장 왼쪽 아래 모서리
people = [list(map(int, input().split())) for _ in range(P)]
# 검사할 사람의 좌표를 리스트로 받아 people 리스트에 저장

cnt = 0                                                     # 경기장 내 사람의 수를 셀 변수를 만듬
while people:                                               # 검사를 받을 사람의 좌표가 들어 있는 리스트가 빌때까지 반복
    p = people.pop(0)                                       # 리스트에서 좌표를 하나 꺼내 p에 저장한 후
    if X <= p[0] <= X + W:                                  # 검사하려는 사람의 좌표가 경기장의 직사각형 영역의 가로 영역 내에 있을 때
        if Y <= p[1] <= Y + H:                              # 검사하려는 사람의 좌표가 경기장의 직사각형 영역의 세로 영역 내에 있으면 한명을 세고
            cnt += 1
        else:                                               # 밖에 있으면 건너 뛴다
            pass
    elif X > p[0]:                                          # 검사하려는 사람의 좌표가 직사각형 영역보다 더 왼쪽에 있다면
        if H//2 >= math.dist([X, Y + H//2], p):             # 검사하려는 사람의 좌표가 왼쪽 반원의 중심으로 반지름내 있는지 확인해서 반지름 내에 있다면 한명을 세고
            cnt += 1
        else:                                               # 밖에 있으면 건너 뛴다
            pass
    elif p[0] > X + W:                                      # 검사하려는 사람의 좌표가 직사각형 영역보다 더 오른쪽에 있다면
        if H//2 >= math.dist([X + W, Y + H//2], p):         # 검사하려는 사람의 좌표가 오른쪽 반원의 중심으로 반지름내 있는지 확인해서 반지름 내에 있다면 한명을 세고
            cnt += 1
        else:                                               # 밖에 있으면 건너 뛴다
            pass

print(cnt)