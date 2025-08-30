# 브실혜성_BOJ29722

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
y, m, d = map(int, input().split('-'))  # 날짜를 input받고
N = int(input())                        # 브실컵까지 남은 날짜를 input받고
Y = N // 360                            # 남은 연도를 구하고
M = (N%360) // 30                       # 남은 월을 구하고
D = N%30                                # 남은 일을 구해서
if D + d > 30:                          # 현재 일에 계산한 일을 더해서 한달을 초과하면
    M += 1                              # 한달을 추가하고
    d -= 30                             # 30일을 빼준 후
d += D                                  # 브실컵이 일어나는 일을 더해준다
if M + m > 12:                          # 현재 월에 계산한 월을 더해서 일년을 초과하면
    Y += 1                              # 일년을 추가하고
    M -= 12                             # 12개월을 빼준 후
m += M                                  # 브실컵이 일어나는 월을 더해준다
y += Y                                  # 브실컵이 일어나는 년을 더해준다
if m < 10:                              # 한자리수 달이라면
    m = '0'+str(m)                      # 앞에 0을 붙여주고
if d < 10:                              # 한자리수 일이라면
    d = '0'+str(d)                      # 앞에 0을 붙여주고 
print(f'{y}-{m}-{d}')                   # 브실컵이 일어나는 날을 출력한다