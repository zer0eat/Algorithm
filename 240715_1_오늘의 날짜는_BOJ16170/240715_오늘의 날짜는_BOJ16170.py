# 오늘의 날짜는_BOJ16170

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import datetime

# input 받기
data = datetime.datetime.now() + datetime.timedelta(hours=9) # 현재 시간을 저장하고
print(data.year)    # 년을 출력하고
print(data.month)   # 월을 출력하고
print(data.day)     # 일을 출력한다
