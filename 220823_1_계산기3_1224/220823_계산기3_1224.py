# 계산기3_1224

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10
for t in range(T):
    N = int(input())
    calculator = input()

    # 후위 계산식 만들기
    stack = []
    postfix = []
    for c in calculator:
        if c == '*' or c == '/':
            while stack:
                if stack[-1] == '+' or stack[-1] == '-':
                    break
                elif stack[-1] == '*' or stack[-1] == '/':
                    postfix.append(stack.pop())  # 스택에서 pop해서 postfix에 append 한다
                elif stack[-1] == '(':  # * 연산자가 나올때까지
                    break

            stack.append(c)

        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':  # * 연산자가 나올때까지
                postfix.append(stack.pop())  # 스택에서 pop해서 postfix에 append 한다
            stack.append(c)

        elif c == '(':
            stack.append(c)

        elif c == ')':
            while stack and stack[-1] != '(':  # * 연산자가 나올때까지
                if stack[-1] != '(':
                    postfix.append(stack.pop())  # 스택에서 pop해서 postfix에 append 한다
            stack.pop()

        else:
            postfix.append(int(c))
    else:
        while stack:
            postfix.append(stack.pop())


    # 계산하기
    stack = []  # 계산하기 위한 빈 스택을 리스트로 만듬
    for c in postfix:  # 계산식을 반복할 때
        if c == '+':  # + 연산자가 나오면
            if len(stack) >= 2:  # 스택에 쌓인 숫자가 2개 이상일 때
                b = stack.pop()  # 스택에서 먼저 꺼낸 것을 b
                a = stack.pop()  # 스택에서 나중에 꺼낸 것을 a라고 하고
                stack.append(a + b)  # a와 b를 +로 연산한 값을 스택에 append
            else:  # 만약 스택에 숫자 2개 미만이라면
                print(f'#{t + 1}', 'error')  # 계산이 불가하므로 error를 출력하고 break
                break
        elif c == '-':  # - 연산자가 나오면
            if len(stack) >= 2:  # 스택에 쌓인 숫자가 2개 이상일 때
                b = stack.pop()  # 스택에서 먼저 꺼낸 것을 b
                a = stack.pop()  # 스택에서 나중에 꺼낸 것을 a라고 하고
                stack.append(a - b)  # a와 b를 -로 연산한 값을 스택에 append
            else:  # 만약 스택에 숫자 2개 미만이라면
                print(f'#{t + 1}', 'error')  # 계산이 불가하므로 error를 출력하고 break
                break
        elif c == '*':  # * 연산자가 나오면
            if len(stack) >= 2:  # 스택에 쌓인 숫자가 2개 이상일 때
                b = stack.pop()  # 스택에서 먼저 꺼낸 것을 b
                a = stack.pop()  # 스택에서 나중에 꺼낸 것을 a라고 하고
                stack.append(a * b)  # a와 b를 *로 연산한 값을 스택에 append
            else:  # 만약 스택에 숫자 2개 미만이라면
                print(f'#{t + 1}', 'error')  # 계산이 불가하므로 error를 출력하고 break
                break
        elif c == '/':  # / 연산자가 나오면
            if len(stack) >= 2:  # 스택에 쌓인 숫자가 2개 이상일 때
                b = stack.pop()  # 스택에서 먼저 꺼낸 것을 b
                a = stack.pop()  # 스택에서 나중에 꺼낸 것을 a라고 하고
                stack.append(a // b)  # a와 b를 //(나머지가 없다는 조건이 있으므로)로 연산한 값을 스택에 append
            else:  # 만약 스택에 숫자 2개 미만이라면
                print(f'#{t + 1}', 'error')  # 계산이 불가하므로 error를 출력하고 break
                break
        elif c == '.':  # .이 나오면
            pass  # pass
        else:  # 연산식과 .을 제외한 숫자가 나오면
            stack.append(int(c))  # 스택에 int 형태로 append

    else:  # 반복문을 마쳤다면
        if len(stack) == 1:  # stack의 길이가 1일때
            print(f'#{t + 1}', stack[0])  # 연산결과를 출력한다
        else:  # 그 외의 경우는 연산 실패이므로
            print(f'#{t + 1}', 'error')  # error를 출력