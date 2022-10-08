# 균형잡힌세상_BOJ4949

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                                # break가 될때까지 반복할 때
    stack = []                                          # 스택으로 사용할 빈리스트를 생성하고
    word = list(sys.stdin.readline().rstrip())          # word에 문장을 리스트로 input 받는다
    if word == ['.']:                                   # 만약 word에 input 받은 내용이 . 하나라면 반복문을 종료한다
        break

    for w in word:                                      # word의 단어를 하나씩 반복해서
        if w == '(' or w == '[':                        # ( 여는소괄호나 [ 여는대괄호가 나오면
            stack.append(w)                             # stack에 append

        elif w == ')':                                  # 닫는 소괄호가 나오면
            if len(stack) == 0 or stack[-1] == '[':     # 스택이 비어있거나 스택의 top이 여는대괄호이면
                print('no')                             # no를 출력하고 while문을 종료한다
                break
            elif stack[-1] == '(':                      # 스택의 top이 여는소괄호이면
                stack.pop()                             # stack에서 top을 pop

        elif w == ']':                                  # 닫는 대괄호가 나오면
            if len(stack) == 0 or stack[-1] == '(':     # 스택이 비어있거나 스택의 top이 여는소괄호이면
                print('no')                             # no를 출력하고 while문을 종료한다
                break
            elif stack[-1] == '[':                      # 스택의 top이 여는소괄호이면
                stack.pop()                             # stack에서 top을 pop
    else:                                               # word의 단어를 모두 탐색했다면
        if len(stack) == 0:                             # 스택이 비어있을 경우
            print('yes')                                # yes를 출력하고
        else:                                           # 스택이 남아있는 경우
            print('no')                                 # no를 출력한다