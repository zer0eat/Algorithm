# 숭고한에 어서오세요_BOJ34236

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 대회가 열린 개수를 input받고
A = list(map(int, input().split()))     # 대회가 열린 연도를 리스트로 input받고
print(A[-1]+A[1]-A[0])                  # 다음 대회가 열리는 연도를 출력한다 (마지막 대회 연도 + (두번째 대회 연도 - 첫번째 대회 연도))