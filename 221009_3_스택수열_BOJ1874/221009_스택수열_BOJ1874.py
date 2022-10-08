# 스택수열_BOJ1874

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
n = int(sys.stdin.readline())           # n 1부터 n까지 정수의 마지막 수
maxn = 0                                # 숫자를 하나씩 input 받을 때 현재까지의 최대값
stack = []                              # 스택으로 사용할 빈리스트 생성
ans = []                                # 정답을 저장할 빈 리스트 생성
i = 1                                   # 스택에 쌓을 정수
for _ in range(n):                      # n개의 정수를 반복할 때
    a = int(sys.stdin.readline())       # a에 정수를 하나 input 받고
    if maxn < a:                        # a가 현재 최대값보다 클 때
        maxn = a                        # 현재 최대값을 a로 바꿔준다
    elif maxn > a and stack[-1] > a:    # a가 현재 최대값보다 작고, 쌓인 스택의 top보다 작을 때
        print('NO')                     # 출력할 수 없으므로 NO를 출력하고 반복문을 종료한다
        break
    while 1:                            # break로 종료될때까지 반복해서
        if stack and stack[-1] == a:    # 빈 스택이 아니면서 스택의 top이 a이면
            stack.pop()                 # 스택의 top을 pop하고
            ans.append('-')             # ans에 -를 append
            break
        else:                           # 스택의 top이 a가 아니면
            stack.append(i)             # i를 스택에 append하고
            if i <= n:                  # i가 n보다 작은 정수라면
                i += 1                  # i에 1을 추가한다
                ans.append('+')         # ans에 +를 append
else:                                   # 순서대로 출력했다면
    for p in ans:                       # 정답에 저장했던 +,-를
        print(p)                        # 순서에따라 하나씩 출력한다
