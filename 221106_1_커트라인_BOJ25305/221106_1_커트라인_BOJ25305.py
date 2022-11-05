# 커트라인_BOJ25305

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, k = map(int, sys.stdin.readline().split())           # N 응시자의 수 / k 수상자 수
rank = list(map(int, sys.stdin.readline().split()))     # 응시자의 성적을 리스트에 담아

rank.sort(reverse=True)                                 # 내림차순으로 정렬한다

print(rank[k-1])                                        # 수상자 중 마지막 사람의 점수를 출력하여 커트라인을 출력한다