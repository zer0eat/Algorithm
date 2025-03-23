# 그게 무슨 코드니.._BOJ31495

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = input().strip()                 # 문자를 input 받고
if N[0] == '"' and N[-1] == '"':    # 문자 양 옆에 ""가 있다면
    if len(list(N[1:-1])) != 0:     # 문자가 없을 경우
        print(N[1:-1])              # CE를 출력하고
    else:                           # 문자가 있을 경우
        print('CE')                 # 문자를 출력하고
else:                               # ""가 없을 경우
    print('CE')                     # CE를 출력한다