# 좌표정렬하기_BOJ11651

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                                                # 좌표의 개수를 받고
arr = []                                                        # 빈 리스트를 만든 후
for n in range(N):                                              # 좌표의 개수만큼 반복해서
    x, y = map(int, input().split())
    arr.append([y,x])                                           # arr에 좌표를 반대로 append

arr.sort()                                                      # 좌표 정렬

for a in arr:
    print(a[1], a[0])                                           # x좌표부터 출력