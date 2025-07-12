# 콘서트_BOJ16466

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 팔린 표의 수를 input받고
A = list(map(int, input().split()))     # 표의 번호를 반복해서
A.sort()                                # 표를 오름차순으로 정렬한다
tmp = 1                                 # 표 번호를 변수로 생성하고
while 1:                                # break가 나올 때까지 반복해서
    if tmp > N:                         # 팔린 티켓을 다 확인했다면
        print(tmp)                      # 현재 티켓 번호를 출력하고
        break                           # while문을 종료한다
    if A[tmp-1] != tmp:                 # 티켓번호가 순서에 맞지 않다면
        print(tmp)                      # 현재 티켓 번호를 출력하고
        break                           # while문을 종료한다
    else:                               # 티켓번호가 순서에 맞다면
        tmp += 1                        # 다음 티켓으로 넘어간다