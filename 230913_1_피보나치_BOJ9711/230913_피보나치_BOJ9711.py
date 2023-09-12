# 피보나치_BOJ9711

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                                    # 테스트 케이스를 input 받고
lst = []                                                            # 테스트 케이스마다 피보나치 수와 나눌 숫자를 저장할 리스트를 생성한다
num = 0                                                             # 구하고자하는 최대 피보나치수를 저장할 변수를 생성하고
for t in range(T):                                                  # 테스트 케이스를 반복해서
    a, b = map(int, input().split())                                # 피보나치수의 번호와 피보나치 수를 나눌 수를 input 받아서
    lst.append([a, b])                                              # lst에 input하고
    if num < a:                                                     # num보다 a가 더 크다면
        num = a                                                     # num에 a를 저장한다
fibonacci = [1, 1]                                                  # 피보나치 수를 저장할 리스트를 1, 2번째 피보나치 수를 넣어 생성하고
for i in range(2, num):                                             # 3번째 피보나치수 부터 num에 저장된 최대 번호까지 반복해서
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])               # 피보나치수를 구해서 리스트에 append한다
for t in range(T):                                                  # 테스트 케이스를 반복해서
    print(f'Case #{t+1}:', fibonacci[lst[t][0]-1] % lst[t][1])      # 테스트 케이스와 해당 인덱스의 피보나치수를 나눈 나머지를 출력한다