# 데칼코마니_BOJ23841

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # 행과 열의 길이를 input 받고
for n in range(N):                  # 행의 크기만큼 반복해서
    A = list(input().strip())       # 한 행을 리스트로 input받고
    for m in range(M//2):           # 한 행의 반만 반복해서
        if A[m] != '.':             # m번째가 .이 아니라면
            A[M-m-1] = A[m]         # 반대편에 색을 칠해주고
        else:                       # m번째가 .이라면
            A[m] = A[M-m-1]         # 반대편의 색을 m번째에 칠해준다
    for a in A:                     # 행을 반복해서
        print(a, end='')            # 데칼코마니한 색을 출력하고
    print()                         # 한줄 넘어간다