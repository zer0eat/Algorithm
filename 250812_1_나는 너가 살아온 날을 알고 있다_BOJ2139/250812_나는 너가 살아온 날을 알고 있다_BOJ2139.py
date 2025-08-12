# 나는 너가 살아온 날을 알고 있다_BOJ2139

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                                # break가 나올때까지 반복해서
    d, m, y = map(int, input().split())                 # 일 월 년을 input받고
    if d == 0 and m == 0 and y == 0:                    # 0,0,0이면
        break                                           # while문을 종료한다
    ans = 0                                             # 정답을 저장할 변수를 생성하고
    if y % 400 == 0 or (y % 100 and y % 4 == 0):        # 400으로 나눠떨어지거나 4로 나눠떨어지면서 100으로 나눠떨어지지 않으면
        L = [31,29,31,30,31,30,31,31,30,31,30,31]       # 윤년으로 계산하고
    else:                                               # 그렇지 않다면
        L = [31,28,31,30,31,30,31,31,30,31,30,31]       # 평년으로 계산해서
    for n in range(m-1):                                # 월을 반복해서
        ans += L[n]                                     # 일을 더해주고
    else:                                               # 해당월만 남았다면
        ans += d                                        # 해당월에 일을 더해주고
    print(ans)                                          # 정답을 출력한다