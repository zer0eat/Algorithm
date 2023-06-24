# 토너먼트_BOJ1057

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
N, kim, lim = map(int, input().split()) # N 참가자의 수 / kim 김지민의 참가번호 / lim 임한수의 참가번호를 input
cnt = 1                                 # 라운드 번호를 셀 변수 생성
while 1:                                # break가 나올 때까지 반복해서
    kim = math.ceil(kim/2)              # kim을 2로 나눈 값을 올림하고
    lim = math.ceil(lim/2)              # lim을 2로 나눈 값을 올림해서
    if kim == lim:                      # 두 수가 같아진다면
        print(cnt)                      # 대결할 라운드가 찾아왔으므로 cnt를 출력하고
        break                           # while문 break
    cnt += 1                            # 두 수가 같지 않은 경우에는 cnt를 1 올려 다음 라운드를 탐색한다