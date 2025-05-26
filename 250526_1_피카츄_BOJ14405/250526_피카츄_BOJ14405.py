# 피카츄_BOJ14405

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = input().strip()             # 문장을 input받고
n = 0                           # 위치를 표시할 변수를 생성한다
while n < len(S):               # 문장의 길이 안에 있다면 반복해서
    if S[n] == 'p':             # n번째 글자가 p라면
        if S[n:n+2] == 'pi':    # n부터 n+1까지 pi라면
            n += 2              # 인덱스를 두칸 이동한다
        else:                   # n부터 n+1까지 pi가 아니라면
            print('NO')         # NO를 출력하고
            break               # while문을 break한다
    elif S[n] == 'k':           # n번째 글자가 k라면
        if S[n:n+2] == 'ka':    # n부터 n+1까지 ka라면
            n += 2              # 인덱스를 두칸 이동한다
        else:                   # n부터 n+1까지 ka가 아니라면
            print('NO')         # NO를 출력하고
            break               # while문을 break한다
    elif S[n] == 'c':           # n번째 글자가 c라면
        if S[n:n+3] == 'chu':   # n부터 n+2까지 chu라면
            n += 3              # 인덱스를 세칸 이동한다
        else:                   # n부터 n+2까지 chu가 아니라면
            print('NO')         # NO를 출력하고
            break               # while문을 break한다
    else:                       # n번째 글자가 p,k,c가 아니라면
        print('NO')             # NO를 출력하고
        break                   # while문을 break한다
else:                           # 모두 통과했다면
    print('YES')                # YES를 출력한다