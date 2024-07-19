# 카드 뽑기_BOJ16204

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, K = map(int, input().split()) # N 카드의 개수 / M O의 개수 / K O로 칠할 개수를 input받고
print(min(N-M, N-K) + min(M,K))     # 앞뒤가 모두 X 것과 모두 O인 것의 합을 출력한다