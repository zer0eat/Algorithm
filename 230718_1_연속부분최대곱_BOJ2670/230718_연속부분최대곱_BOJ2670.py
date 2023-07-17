# 연속부분최대곱_BOJ2670

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 양의 실수의 개수
dp = [0] * N                                    # 연속최대곱을 저장할 리스트 생성
lst = []                                        # 양의 실수를 저장할 리스트 생성
for i in range(N):                              # 양의 실수의 개수만큼 반복해서
    lst.append(float(input()))                  # lst에 양의 실수를 append 하고
    if i == 0:                                  # 첫번째 양의 실수인 경우에는
        dp[i] = lst[i]                          # dp[i]에 첫번째 양의 실수를 저장하고
    else:                                       # 다음부터는
        dp[i] = max(lst[i], dp[i-1] * lst[i])   # dp[i]에 이전까지 최대곱과 현재 실수의 곱과 현재 실수 둘 중 큰 값을 저장한다
print("{:.3f}".format(max(dp)))                 # 연속부분 최대곱을 소수 셋째자리까지 출력한다