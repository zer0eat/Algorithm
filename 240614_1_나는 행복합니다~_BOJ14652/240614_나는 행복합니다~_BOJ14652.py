# 나는 행복합니다~_BOJ14652

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, K = map(int, input().split()) # N 야구장의 행 / M 야구장의 열 / K 좌석번호를 input 받고
print(K//M, K%M)                    # K좌석의 행과 열을 출력한다