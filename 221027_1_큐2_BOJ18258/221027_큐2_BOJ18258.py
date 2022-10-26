# 큐2_BOJ18258

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
T = int(sys.stdin.readline())                   # input 받을 명령의 수
Q = deque()                                     # deque를 생성
for t in range(T):                              # T만큼 반복해서
    A = list(sys.stdin.readline().split())      # A에 input 받아서
    if A[0] == 'push':                          # 앞자리가 push라면
        Q.append(A[1])                          # Q에 뒤에 나오는 숫자를 append한다
    elif A[0] == 'pop':                         # 앞자리가 pop이라면
        if Q:                                   # Q가 비어있지 않다면
            print(Q.popleft())                  # Q의 맨 앞을 pop해서 출력한다
        else:                                   # Q가 비어있다면
            print(-1)                           # -1을 출력한다
    elif A[0] == 'size':                        # 앞자리가 size라면
        print(len(Q))                           # Q의 길이를 출력한다
    elif A[0] == 'empty':                       # 앞자리가 empty라면
        if Q:                                   # Q가 비어있지 않다면
            print(0)                            # 0을 출력한다
        else:                                   # Q가 비어있다면
            print(1)                            # 1을 출력한다
    elif A[0] == 'front':                       # 앞자리가 front라면
        if Q:                                   # Q가 비어있지 않다면
            print(Q[0])                         # Q의 맨앞을 출력한다
        else:                                   # Q가 비어있다면
            print(-1)                           # -1을 출력한다
    elif A[0] == 'back':                        # 앞자리가 back이라면
        if Q:                                   # Q가 비어있지 않다면
            print(Q[-1])                        # Q의 맨뒤를 출력한다
        else:                                   # Q가 비어있다면
            print(-1)                           # -1을 출력한다