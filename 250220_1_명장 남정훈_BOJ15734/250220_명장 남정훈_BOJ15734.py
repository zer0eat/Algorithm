# 명장 남정훈_BOJ15734

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
L, R, A = map(int, input().split()) # 왼발, 오른발, 양발잡이를 input 받고
maxN, minN = max(L, R), min(L, R)   # 왼발 오른발잡이의 최대, 최소값을 구해서
tmp = min(A, maxN-minN)             # 양발잡이를 분배할 수 있는 수를 구한다
minN += tmp                         # 더 적은 곳에 양발잡이를 분배하고
A -= tmp                            # 양발잡이 중 분배 한 수를 빼서
if A:                               # 양발잡이가 남아 있다면
    A = A//2*2                      # 양발잡이의 수를 구하고
print(minN*2 + A)                   # 잔류한 선수를 출력한다