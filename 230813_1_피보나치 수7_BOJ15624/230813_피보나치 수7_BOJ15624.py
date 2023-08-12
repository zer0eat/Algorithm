# 피보나치 수7_BOJ15624

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 구하고 싶은 피보나치 수열의 인덱스를 input 받고
if N == 0:                                          # N이 0인 경우에는
    print(0)                                        # 0을 출력하고
    quit()                                          # 종료한다
fibo = [0, 1]                                       # 0과 1번째 피보나치수를 넣은 리스트를 생성한다
for i in range(2, N+1):                             # 2부터 N까지 반복해서
    fibo[0], fibo[1] = fibo[1] % 1000000007, (fibo[0] + fibo[1]) % 1000000007   # fibo[0]에 i-1번째 피보나치 수를 저장하고 fibo[2]에 i번째 피보나치수를 1000000007로 나눈 나머지를 저장한다
print(fibo[1])                                      # N번째 피보나치수를 출력한다