# 스택2_BOJ28278

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 명령의 수를 input 받고
stack = []                                  # 명령을 저장할 stack을 만든다
for i in range(N):                          # N번의 명령을 반복해서
    a = list(map(int, input().split()))     # 명령을 input 받는다
    if a[0] == 1:                           # 명령 번호가 1번이라면
        stack.append(a[1])                  # input 받은 숫자를 stack에 append 한다
    elif a[0] == 2:                         # 명령 번호가 2번이라면
        if len(stack) > 0:                  # 스택에 정수가 있다면 
            c = stack.pop()                 # 맨 위의 정수를 빼고
            print(c)                        # 해당 정수를 출력한다
        else:                               # 스택에 정수가 없다면
            print(-1)                       # -1을 출력한다
    elif a[0] == 3:                         # 명령 번호가 3번이라면
        print(len(stack))                   # 스택에 들어있는 정수의 개수를 출력한다
    elif a[0] == 4:                         # 명령 번호가 4번이라면
        if len(stack) > 0:                  # 스택이 비어있지 않다면
            print(0)                        # 0을 출력하고
        else:                               # 스택이 비어있으면
            print(1)                        # 1을 출력한다
    else:                                   # 명령 번호가 5번이라면
        if len(stack) > 0:                  # 스택이 비어있지 않다면
            print(stack[-1])                # 맨 위의 정수를 출력하고
        else:                               # 스택이 비어 있다면
            print(-1)                       # -1을 출력한다