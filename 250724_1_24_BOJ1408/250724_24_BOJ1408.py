# 24_BOJ1408

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
time1 = list(input().strip().split(':'))    # 시작 시간을 input받고
time2 = list(input().strip().split(':'))    # 종료 시간을 input받고
s, m, h = (int(time2[2]) - int(time1[2])), (int(time2[1]) - int(time1[1])), (int(time2[0]) - int(time1[0])) # 초, 분, 시를 계산하고
if s < 0 :                                  # 초가 음수라면
    s = 60 + s                              # 양수로 바꿔주고
    m -= 1                                  # 분에서 1분 차감한다
s = str(s)                                  # 초를 문자열로 바꾸고
if len(s) == 1:                             # 초 단위가 한자리라면
    s = '0'+s                               # 앞에 0을 붙여준다
if m < 0 :                                  # 분이 음수라면
    m = 60 + m                              # 양수로 바꿔주고
    h -= 1                                  # 시에서 1시간 차감한다
m = str(m)                                  # 분을 문자열로 바꾸고
if len(m) == 1:                             # 분 단위가 한자리라면
    m = '0'+m                               # 앞에 0을 붙여준다
if h < 0 :                                  # 시가 음수라면
    h = 24 + h                              # 양수로 바꿔주고
h = str(h)                                  # 시를 문자열로 바꾸고
if len(h) == 1:                             # 시가 한자리라면
    h = '0'+h                               # 앞에 0을 붙여준다
print(f'{h}:{m}:{s}')                       # 시, 분, 초를 출력한다