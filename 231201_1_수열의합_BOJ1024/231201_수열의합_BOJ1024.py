# 수열의 합_BOJ1024

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, L = map(int, input().split())            # N 수열의 합 / L 수열의 길이를 input 받고
for n in range(L, 101):                     # L부터 100까지 반복해서
    x = N/n - (n+1)/2                       # n개의 합이 N이 되기 위한 시작값을 구한 후
    if x == int(x):                         # 시작 값이 정수라면
        x = int(x)                          # x를 정수로 변경하고
        if x + 1 >= 0:                      # x+1이 음의정수가 아니라면
            for i in range(x+1, x+1+n):     # x+1부터 n개 반복해서
                print(i, end=' ')           # 원소를 출력하고
            else:                           # 반복을 마쳤다면
                quit()                      # 종료한다
else:                                       # 100개의 합까지 구해도 알맞는 수열이 없다면
    print(-1)                               # -1을 출력한다