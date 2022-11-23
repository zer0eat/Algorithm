# 피보나치수2_BOJ2748

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())           # N 구하고자하는 피보나치 수의 순서
fibo = [0, 1]                           # fibo(0)과 fibo(1)의 값을 넣은 리스트를 생성하고
for n in range(N-1):                    # N번째 피보나치 수를 구하기 위해 필요한 N-1번을 반복해서
    fibo.append(fibo[n] + fibo[n+1])    # Fn = Fn-1 + Fn-2으로 피보나치 수를 계산해서 append

print(fibo[N])                          # N번째 피보나치 수를 출력한다