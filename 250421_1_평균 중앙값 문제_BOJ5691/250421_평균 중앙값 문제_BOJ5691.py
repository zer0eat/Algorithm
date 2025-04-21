# 평균 중앙값 문제_BOJ5691

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                # break가 나올 때까지 반복해서
    a, b = map(int, input().split())    # 두 수를 input 받고
    if a == 0 and b == 0:               # 두 수 모두 0이라면
        break                           # while문을 종료하고
    print(a-abs(a-b))                   # a가 중앙값이고 b가 최대값일 때 최소값을 출력한다