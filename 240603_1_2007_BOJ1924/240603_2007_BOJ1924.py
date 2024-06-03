# 2007_BOJ1924

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
x, y = map(int, input().split())                        # x월 y일을 input 받고
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    # 매월 일 수를 저장한 리스트를 생성하고
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] # 요일을 저장한 리스트를 생성한다
ans = 0                                                 # 일수를 계산할 변수를 생성하고
for n in range(x-1):                                    # x월 이전까지 반복해서
    ans += d[n]                                         # 해당 월의 일 수를 ans에 더해주고
ans += y                                                # y일을 ans에 더해준다
print(day[ans % 7])                                     # x월 y일이 무슨 요일인지 출력한다