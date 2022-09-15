# 좌표정렬하기_BOJ11650

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                                   # 좌표의 개수를 받고
arr = []                                                        # 빈 리스트를 만든 후
for n in range(N):                                              # 좌표의 개수만큼 반복해서
    arr.append(list(map(int, sys.stdin.readline().split())))    # arr에 좌표를 append

arr.sort()                                                      # 좌표 정렬

for a in arr:
    print(*a)