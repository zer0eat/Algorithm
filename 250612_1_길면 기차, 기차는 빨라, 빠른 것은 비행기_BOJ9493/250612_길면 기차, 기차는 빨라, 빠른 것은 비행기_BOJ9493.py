# 길면 기차, 기차는 빨라, 빠른 것은 비행기_BOJ9493

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                                # break가 나올때 까지 반복해서
    m, a, b = map(int, input().split())                 # 거리 기차속도 비행기속도를 input받고
    if m == a == b == 0:                                # 세 수가 모두 0이라면
        break                                           # while문을 종료한다
    t = round(((m/a)-(m/b)) * 3600)                     # 기차와 비행기 탔을 때 시간 차를 구해서
    print("%d:%02d:%02d" %(t//3600, t%3600//60, t%60))  # 시간 차이를 시 분 초로 출력한다