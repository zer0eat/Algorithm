# 욱제는 효도쟁이야!!_BOJ14487

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 마을의 수를 input받고
V = list(map(int, input().split())) # 이동 비용을 리스트로 input받고
print(sum(V)-max(V))                # 최소 이동비용을 출력한다