# 알고리즘수업-피보나치함수1_BOJ24416

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def fib(n):                             # 재귀로 피보나치 돌리기 위한 함수
    global cntfib                       # cntfib를 불러와서
    if n == 1 or n == 2:                # 1이나 2가 나왔을 때
        cntfib += 1                     # 1을 추가하고
        return 1
    else:                               # 1이나 2가 아니라면
        return fib(n - 1) + fib(n - 2)  # 재귀로 1과 2를 찾을 떄까지 반복한다

def fibonacci(n):                       # 동적계획법으로 피보나치를 돌리기 위한 함수
    global cntfibonacci                 # cntfibonacci를 불러와서
    f = [0, 1, 1]                       # 0,1,2 일때 결과 값을 넣은 리스트를 생성한다.
    for i in range(3, n+1):             # 3부터 N까지 반복해서
        cntfibonacci += 1               # 반복회수를 추가하고
        f.append(f[i - 1] + f[i - 2])   # 해당 숫자의 값을 f에 append 한다


# input 받기
N = int(sys.stdin.readline())           # 피보나치 수를 구하기 위한 N
cntfib = 0                              # 재귀로 풀었을 때 반복 횟수
cntfibonacci = 0                        # 동적계획법으로 풀었을 때 반복 횟수

fib(N)                                  # 재귀로 돌리고
fibonacci(N)                            # 동적계획법으로 돌려서

print(cntfib, cntfibonacci)             # 각각의 횟수를 출력한다

