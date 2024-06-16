# 특별한 날_BOJ10768

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
M = int(input())            # 달을 input 받고
D = int(input())            # 일을 input 받아서
if M < 2:                   # 1월이라면
    print('Before')         # Before를 출력하고
elif M == 2:                # 2월인데
    if D < 18:              # 18일 전이라면
        print('Before')     # Before를 출력하고
    elif D == 18:           # 18일이라면
        print('Special')    # Special를 출력하고
    else:                   # 18일 이후라면
        print('After')      # After를 출력하고
else:                       # 3월 이상이라면
    print('After')          # After를 출력한다