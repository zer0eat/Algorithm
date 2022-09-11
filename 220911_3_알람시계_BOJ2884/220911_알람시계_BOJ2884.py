# 알람시계_BOJ2884

# input.txt
import sys
sys.stdin = open('input3.txt')

# input 받기
H, M = map(int, input().split())    # 시와 분을 input 받기

# 45분 전으로 시간 바꾸기
M = M - 45                          # input 받은 분에서 45분 전으로 돌리기
if M < 0:                           # 45분 전이 음수가 되었다면
    M = M + 60                      # 60을 더해 분을 설정하고
    H = H - 1                       # 시간을 한 시간 전으로 설정한다
    if H < 0:                       # 시간이 음수가 되었다면
        H = H + 24                  # 24를 더해 시간을 설정해준다

print(H, M)