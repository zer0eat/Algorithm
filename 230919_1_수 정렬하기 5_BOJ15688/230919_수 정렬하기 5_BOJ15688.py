# 수 정렬하기 5_BOJ15688

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                        # 정렬할 수의 개수를 input 받고
lst = []                                # 저장할 리스트를 생성하고
for i in range(N):                      # 정렬할 수의 개수를 반복해서
    heapq.heappush(lst, int(input()))   # 정렬할 수를 input 받아 lst에 heappush 한다
for i in range(N):                      # 정렬할 수의 개수를 반복해서
    print(heapq.heappop(lst))           # lst에서 heappop해서 비내림차순으로 정렬한 결과를 한 줄에 하나씩 출력한다