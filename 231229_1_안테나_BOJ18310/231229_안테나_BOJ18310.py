# 안테나_BOJ18310

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input.txt 열기
N = int(input())                        # 집의 수를 input 받고
house = list(map(int, input().split())) # 집의 위치를 input 받아 list에 저장한 후
house.sort()                            # 오름차순으로 정렬한다
if N % 2:                               # 집의 개수가 홀수라면
    print(house[N//2])                  # 가운데 집의 위치를 출력하고
else:                                   # 집의 개수가 짝수라면
    print(house[N//2-1])                # 중간의 두 집 중 앞에 집의 위치를 출력한다