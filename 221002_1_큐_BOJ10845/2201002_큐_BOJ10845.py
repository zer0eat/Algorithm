# 큐_BOJ10845

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                   # N = 명령의 수
q = []                                          # 큐를 쌓을 빈 리스트 생성
for n in range(N):                              # 명령의 수만큼 반복할 때
    a = list(sys.stdin.readline().split())      # a에 명령을 input 받고
    if a[0] == 'push':                          # a[0]이 push라면
        q.append(a[1])                          # a[1]을 q에 append
    elif a[0] == 'pop':                         # a[0]이 pop이라면
        if len(q) == 0:                         # q가 비어있을 때
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(q.pop(0))                     # 맨앞에서 q를 빼서 출력한다
    elif a[0] == 'size':                        # a[0]이 size라면
        print(len(q))                           # q의 길이를 출력한다
    elif a[0] == 'empty':                       # a[0]이 empty라면
        if len(q) == 0:                         # q가 비어있다면
            print(1)                            # 1을 출력하고
        else:                                   # 그렇지 않으면
            print(0)                            # 0을 출력한다
    elif a[0] == 'front':                       # a[0]이 front라면
        if len(q) == 0:                         # q가 비어있으면
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(q[0])                         # q의 맨앞을 출력한다
    elif a[0] == 'back':                        # a[0]이 back이라면
        if len(q) == 0:                         # q가 비어있으면
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(q[-1])                        # q의 마지막을 출력한다