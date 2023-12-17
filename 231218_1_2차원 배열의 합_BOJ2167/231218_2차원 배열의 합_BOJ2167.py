# 2차원 배열의 합_BOJ2167

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                            # N 배열의 행 / M 배열의 열의 크기를 input 받고
lst = [list(map(int, input().split())) for _ in range(N)]   # 배열을 input 받아 lst에 저장한다
K = int(input())                                            # 합을 구할 부분의 수를 input 받고
for k in range(K):                                          # 합을 구할 부분의 수만큼 반복해서
    i, j, x, y = map(int, input().split())                  # 합을 구할 부분의 왼쪽 위 i,j와 오른쪽 아래 x,y를 input 받고
    ans = 0                                                 # 합을 저장할 변수를 생성하고
    for q in range(x-i+1):                                  # 합을 구할 부분의 행을 반복해서
        ans += sum(lst[i-1+q][j-1:y])                       # 해당 행의 합을 구할 열의 합을 ans에 저장한다
    print(ans)                                              # 배열의 합을 출력한다