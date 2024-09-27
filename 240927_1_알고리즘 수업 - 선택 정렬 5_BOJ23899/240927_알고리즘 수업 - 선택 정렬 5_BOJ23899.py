# 알고리즘 수업 - 선택 정렬 5_BOJ23899

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 정렬할 배열의 크기를 input 받고
A = list(map(int, input().split())) # 시작 배열을 input 받고
B = list(map(int, input().split())) # 정렬 중간에 나올 배열을 input 받아서
if A == B:                          # 선택정렬 중 B가 나온다면
    print(1)                        # 1을 출력하고
    quit()                          # 종료한다
for n in range(N-1, -1, -1):        # 시작점을 반복하고
    tmp = n                         # 바꿀 원소의 인덱스를 저장할 변수를 생성하고
    for m in range(n-1, -1, -1):    # 바꿀점을 반복해서
        if A[m] > A[tmp]:           # 더 큰수가 나온다면
            tmp = m                 # 더 큰수의 위치를 저장한다
    else:                           # 배열을 반복한 후
        A[tmp], A[n] = A[n], A[tmp] # n번째 앞에 가장 큰 수를 n번째에 저장한다
    if A == B:                      # 선택정렬 중 B가 나온다면
        print(1)                    # 1을 출력하고
        quit()                      # 종료한다
print(0)                            # 선택정렬 중 B가 안나오면 0을 출력한다