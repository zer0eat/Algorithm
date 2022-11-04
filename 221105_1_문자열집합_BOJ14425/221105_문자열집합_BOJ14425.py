# 문자열집합_BOJ14425

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 기준이 되는 문자열의 수 / M 확인하려는 문자열의 수

Ndict = dict()                                  # N개의 문자열을 저장할 딕셔너리 생성

for _ in range(N):                              # N번 반복하여
    Ndict[input()] = True                       # input 값을 key로 true를 value로 딕셔너리에 추가

cnt = 0
for _ in range(M):                              # M번 반복해서
    if Ndict.get(input()) == True:              # input을 key로 Ndict를 검색했을 때 true라면
        cnt += 1                                # 1을 추가한다

print(cnt)