# 스택_BOJ10828

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                   # N = 명령의 수
stack = []                                      # 스택을 쌓을 빈 리스트 생성
for n in range(N):                              # 명령의 수만큼 반복할 때
    a = list(sys.stdin.readline().split())      # a에 명령을 input 받고
    if a[0] == 'push':                          # a[0]이 push라면
        stack.append(a[1])                      # a[1]을 stack에 append
    elif a[0] == 'pop':                         # a[0]이 pop이라면
        if len(stack) == 0:                     # stack이 비어있을 때
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(stack.pop())                  # 가장 마지막에 넣은 스택을 빼서 출력한다
    elif a[0] == 'size':                        # a[0]이 size라면
        print(len(stack))                       # stack의 길이를 출력한다
    elif a[0] == 'empty':                       # a[0]이 empty라면
        if len(stack) == 0:                     # stack이 비어있다면
            print(1)                            # 1을 출력하고
        else:                                   # 그렇지 않으면
            print(0)                            # 0을 출력한다
    elif a[0] == 'top':                         # a[0]이 top이라면
        if len(stack) == 0:                     # 스택이 비어있으면
            print(-1)                           # -1을 출력하고
        else:                                   # 그렇지 않으면
            print(stack[-1])                    # 스택에서 맨 마지막에 쌓인 부분을 출력한다