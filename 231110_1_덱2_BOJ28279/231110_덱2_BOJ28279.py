# 덱2_BOJ28279

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                            # 명령의 수를 input 받고
deq = deque([])                             # 명령을 수행할 deque을 생성한다
for n in range(N):                          # 명령의 수만큼 반복해서
    a = list(map(int,input().split()))      # 명령을 입력받고
    if a[0] == 1:                           # 명령이 1번이라면
        deq.appendleft(a[1])                # deq의 맨앞에 input받은 숫자를 append한다
    elif a[0] == 2:                         # 명령이 2번이라면
        deq.append(a[1])                    # deq의 맨뒤에 input받은 숫자를 append한다
    elif a[0] == 3:                         # 명령이 3번이라면
        if len(deq):                        # deq이 비어있지 않다면
            print(deq.popleft())            # deq의 맨 앞에서 pop한다
        else:                               # deq이 비어있다면
            print(-1)                       # -1을 출력한다
    elif a[0] == 4:                         # 명령이 4번이라면
        if len(deq):                        # deq이 비어있지 않다면
            print(deq.pop())                # deq의 맨 뒤에서 pop한다
        else:                               # deq이 비어있다면
            print(-1)                       # -1을 출력한다
    elif a[0] == 5:                         # 명령이 5번이라면
        print(len(deq))                     # deq의 길이를 출력한다
    elif a[0] == 6:                         # 명령이 6번이라면
        if len(deq):                        # deq이 비어있지 않다면
            print(0)                        # 0을 출력한다
        else:                               # deq이 비어있다면
            print(1)                        # 1을 출력한다
    elif a[0] == 7:                         # 명령이 7번이라면
        if len(deq):                        # deq이 비어있지 않다면
            print(deq[0])                   # 맨 앞의 원소를 출력한다
        else:                               # deq이 비어있다면
            print(-1)                       # -1을 출력한다
    else:                                   # 명령이 8번이라면
        if len(deq):                        # deq이 비어있지 않다면
            print(deq[-1])                  # 맨 뒤의 원소를 출력한다
        else:                               # deq이 비어있다면
            print(-1)                       # -1을 출력한다