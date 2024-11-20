# 베시와 데이지_BOJ16431

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
Bx, By = map(int, input().split())  # 베시의 위치를 input 받고
Dx, Dy = map(int, input().split())  # 데이지의 위치를 input 받고
Jx, Jy = map(int, input().split())  # 존의 위치를 input 받고
Dtime, Btime = 0, 0                 # 베시와 데이지의 이동시간을 저장할 변수를 생성한다
Dtime = abs(Dx-Jx) + abs(Dy-Jy)     # 데이지의 이동시간을 저장하고
Btime = min(abs(Bx-Jx), abs(By-Jy)) + abs(abs(Bx-Jx) - abs(By-Jy))  # 베시의 이동시간을 저장하고
if Dtime < Btime:                   # 데이지가 이동시간이 짧다면
    print('daisy')                  # 데이지를 출력하고
elif Dtime > Btime:                 # 베시가 이동시간이 짧다면
    print('bessie')                 # 베시를 출력하고
else:                               # 이동시간이 같다면
    print('tie')                    # 같음을 출력한다