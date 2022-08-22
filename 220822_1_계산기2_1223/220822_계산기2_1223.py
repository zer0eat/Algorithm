# 계산기2_1223

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10                                                  # 테스트 케이스
for t in range(T):                                      # 테스트 케이스를 반복할 때
    N = int(input())                                    # 문자열 계산식의 길이
    calculator = input()                                # 문자열 계산식

    # 후위 표기식으로 바꾸기
    stack = []                                          # 후위 표기식을 만들기 위해 사용한 빈 스택을 만들고
    postfix = []                                        # 후위 표기식을 저장할 빈 리스트를 만든다
    for c in calculator:                                # 문자열 계산식을 반복할 때
        if c == '*':                                    # * 연산자가 나오면
            while stack and stack[-1] == '*':           # * 연산자가 나올때까지
                postfix.append(stack.pop())             # 스택에서 pop해서 postfix에 append 한다
            stack.append(c)                             # 그리고 * 연산자를 스택에 append 한다
        elif c == '+':                                  # + 연산자가 나오면
            while stack:                                # 스택이 빌 때까지
                postfix.append(stack.pop())             # 스택에서 pop해서 postfix에 append 한다
            stack.append(c)                             # 그리고 + 연산자를 스택에 append 한다
        else:                                           # 연산자 외 숫자가 나오면
            postfix.append(int(c))                      # int 형태로 append 한다
    while stack:                                        # 반복이 끝났으면
        postfix.append(stack.pop())                     # 스택이 빌때까지 pop해서 postfix에 append 한다

    # 후위 표기식으로 계산하기
    for p in postfix:                                   # 계산식을 반복할 때
        if p == '+':                                    # + 연산자가 나오면
            if len(stack) >= 2:                         # 스택에 쌓인 숫자가 2개 이상일 때
                b = stack.pop()                         # 스택에서 먼저 꺼낸 것을 b
                a = stack.pop()                         # 스택에서 나중에 꺼낸 것을 a라고 하고
                stack.append(a + b)                     # a와 b를 +로 연산한 값을 스택에 append
            else:                                       # 만약 스택에 숫자 2개 미만이라면
                print(f'#{t + 1}', 'error')             # 계산이 불가하므로 error를 출력하고 break
                break
        elif p == '*':                                  # * 연산자가 나오면
            if len(stack) >= 2:                         # 스택에 쌓인 숫자가 2개 이상일 때
                b = stack.pop()                         # 스택에서 먼저 꺼낸 것을 b
                a = stack.pop()                         # 스택에서 나중에 꺼낸 것을 a라고 하고
                stack.append(a * b)                     # a와 b를 *로 연산한 값을 스택에 append
            else:                                       # 만약 스택에 숫자 2개 미만이라면
                print(f'#{t + 1}', 'error')             # 계산이 불가하므로 error를 출력하고 break
                break
        else:                                           # 연산식을 제외한 숫자가 나오면
            stack.append(int(p))                        # 스택에 int 형태로 append
    else:                                               # 반복문을 마쳤다면
        if len(stack) == 1:                             # stack의 길이가 1일때
            print(f'#{t + 1}', stack[0])                # 연산결과를 출력한다
        else:                                           # 그 외의 경우는 연산 실패이므로
            print(f'#{t + 1}', 'error')                 # error를 출력