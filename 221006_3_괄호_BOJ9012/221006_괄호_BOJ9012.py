# 괄호_BOJ9012

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
T = int(sys.stdin.readline())                   # 테스트케이스
for t in range(T):                              # 테스트케이스를 반복할 때
    arr = list(sys.stdin.readline().rstrip())   # 괄호를 arr 에 받고
    arr = deque(arr)                            # arr을 deque로 만들고
    ans = deque([])                             # ans를 deque로 생성한다
    for a in arr:                               # arr을 반복할 때
        if a == '(':                            # (가 나왔다면
            ans.append(a)                       # ans에 append 하고
        elif a == ')':                          # )가 나왔다면
            if len(ans) >= 1:                   # ans에 (가 들어있다면
                ans.pop()                       # 하나를 빼고
            elif len(ans) == 0:                 # 없다면
                print('NO')                     # NO를 프린트하고 반복문을 종료한다
                break
    else:                                       # 반복문을 완료했을 때
        if len(ans) >= 1:                       # ans가 비어있지 않다면
            print('NO')                         # (가 남아 있으므로 NO 출력
        elif len(ans) == 0:                     # ans가 비어있다면
            print('YES')                        # 괄호가 완벽하므로 YES 출력