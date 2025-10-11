# 강의실 예약 시스템_BOJ30019

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # 강의실의 수와 빌리려는 사람을 input받고
lst = [0]*N                             # 강의실 대여 정보를 저장할 리스트를 생성하고
for m in range(M):                      # 빌리려는 사람을 반복해서
    k, s, e = map(int, input().split()) # 강의실번호와 시작과 끝 시간을 input받고
    if lst[k-1] <= s:                   # 시작 시간에 강의실을 쓸 수 있다면
        print('YES')                    # 네를 출력하고
        lst[k-1] = e                    # 종료시간을 저장한다
    else:                               # 시작 시간에 강의실을 쓸 수 없다면
        print('NO')                     # 아니오를 출력한다