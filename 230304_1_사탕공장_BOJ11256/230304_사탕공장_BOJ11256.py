# 사탕공장_BOJ11256

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
T = int(input())                            # T 테스트케이스
for _ in range(T):                          # 테스트케이스를 반복해서
    J, N = map(int, input().split())        # J 사탕의 개수 / N 박스의 수
    box = []                                # 박스를 담을 리스트 생성
    for _ in range(N):                      # 박스의 수만큼 반복해서
        i, c = map(int, input().split())    # 박스의 가로와 세로의 길이를 input 받고
        box.append(i*c)                     # 박스의 넓이를 box에 append
    box.sort(reverse=True)                  # box를 내림차순으로 sort하고
    box = deque(box)                        # box를 deque로 바꾼 후
    cnt = 0                                 # 횟수를 저장할 변수를 생성한다
    while J > 0:                            # J가 0보다 작아질때까지 반복해서
        cnt += 1                            # 변수를 1 더하고
        a = box.popleft()                   # box에서 가장 큰 수를 pop한 후
        J -= a                              # J에서 그 수를 빼준다
    else:                                   # while문을 마쳤다면
        print(cnt)                          # cnt를 출력한다