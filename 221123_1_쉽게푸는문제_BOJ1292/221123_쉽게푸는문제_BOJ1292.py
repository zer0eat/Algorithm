# 쉽게푸는문제_BOJ1292

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 더하려는 값의 시작순서 M 더하려는 값의 마지막순서

lst = []                                        # 빈 리스트를 생성하고

cnt = 1                                         # cnt에 1을 저장하고
while cnt <= M:                                 # cnt가 M보다 커질때까지 반복해서
    for c in range(cnt):                        # cnt 만큼 반복해서
        lst.append(cnt)                         # lst에 cnt를 넣는다
    else:                                       # 반복을 마쳤다면
        cnt += 1                                # cnt에 1을 추가한다
    
print(sum(lst[N-1:M]))                          # N부터 M까지 숫자를 더한 값을 출력한다