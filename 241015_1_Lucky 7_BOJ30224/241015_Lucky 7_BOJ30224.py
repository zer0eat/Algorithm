# Lucky 7_BOJ30224

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = input().strip() # 숫자를 input 받고
if '7' in N:        # 7이 들어있으면
    if int(N)%7:    # 7로 나눠떨어지지 않으면
        print(2)    # 2를 출력한다
    else:           # 7로 나눠떨어지면
        print(3)    # 3을 출력한다
else:               # 7이 없으면
    if int(N)%7:    # 7로 나눠떨어지지 않으면
        print(0)    # 0을 출력한다
    else:           # 7로 나눠떨어지면
        print(1)    # 1을 출력한다