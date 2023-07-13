# 피보나치 수 4_BOJ10826

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                        # 구하고자하는 피보나치 수의 인덱스를 input 받고
fibonacci = [0, 1]                                      # 0, 1번째 피보나치 수를 넣은 리스트를 생성한다
for i in range(2, N+1):                                 # 2번째 부터 N번째까지 반복해서
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])   # i번째 피보나치 수열을 리스트에 append
print(fibonacci[N])                                     # N번째 피보나치 수를 출력한다