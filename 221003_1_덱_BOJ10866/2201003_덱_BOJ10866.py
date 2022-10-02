# 덱_BOJ10866

# input.txt 열기
import sys
from collections import deque
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                   # N = 명령의 수
q = []                                          # 큐를 쌓을 빈 리스트 생성
deq = deque(q)                                  # q를 deque로 설정하고 deq로 명명

for n in range(N):                              # 명령의 수만큼 반복할 때
    a = list(sys.stdin.readline().split())      # a에 명령을 input 받고
    if a[0] == 'push_front':                    # a[0]이 push_front라면
        deq.appendleft(a[1])                    # a[1]을 deq에 appendleft
    elif a[0] == 'push_back':                   # a[0]이 push_back라면
        deq.append(a[1])                        # a[1]을 deq에 append

    elif a[0] == 'pop_front':                   # a[0]이 pop_front이라면
        if len(deq) == 0:                       # deq가 비어있을 때
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(deq.popleft())                # 맨앞에서 deq를 빼서 출력한다
    elif a[0] == 'pop_back':                    # a[0]이 pop_back이라면
        if len(deq) == 0:                       # deq가 비어있을 때
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(deq.pop())                    # 맨앞에서 deq를 빼서 출력한다

    elif a[0] == 'size':                        # a[0]이 size라면
        print(len(deq))                         # deq의 길이를 출력한다
    elif a[0] == 'empty':                       # a[0]이 empty라면
        if len(deq) == 0:                       # deq가 비어있다면
            print(1)                            # 1을 출력하고
        else:                                   # 그렇지 않으면
            print(0)                            # 0을 출력한다
    elif a[0] == 'front':                       # a[0]이 front라면
        if len(deq) == 0:                       # deq가 비어있으면
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(deq[0])                       # deq의 맨앞을 출력한다
    elif a[0] == 'back':                        # a[0]이 back이라면
        if len(deq) == 0:                       # deq가 비어있으면
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(deq[-1])                      # deq의 마지막을 출력한다