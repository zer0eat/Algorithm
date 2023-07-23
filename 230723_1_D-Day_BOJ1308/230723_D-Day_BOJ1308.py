# D-Day_BOJ1308

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import datetime

# input 받기
today = list(map(int, input().split()))                         # 오늘 날짜를 리스트로 input 받고
dday = list(map(int, input().split()))                          # d-day 날짜를 리스트로 input 받는다
today_datetime = datetime.date(today[0], today[1], today[2])    # 오늘 날짜를 datetime형식으로 저장하고
after_1000y = datetime.date(today[0]+1000, today[1], today[2])  # 1000년 후 날짜를 datetime형식으로 저장하고
dday_datetime = datetime.date(dday[0], dday[1], dday[2])        # d-day 날짜를 datetime형식으로 저장한다
if dday_datetime-today_datetime < after_1000y-today_datetime:   # 만약 d-day까지 남은 날이 1000년 미만이라면
    print("D-{}".format((dday_datetime-today_datetime).days))   # d-day를 출력하고
else:                                                           # 1000년 이상이라면
    print('gg')                                                 # gg를 출력한다