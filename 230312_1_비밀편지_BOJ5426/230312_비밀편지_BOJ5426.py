# 비밀편지_BOJ5426

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
T = int(input())                            # 테스트케이스
for t in range(T):                          # 테스트케이스르 반복해서
    A = input().strip()                     # A에 암호화된 문자열을 input 받는다
    a = round(math.sqrt(len(A)))            # A 길이의 제곱근을 a에 저장하고
    ans = ''                                # 복호화한 정답을 저장할 ans를 생성한다
    for i in range(a-1, -1, -1):            # a-1부터 0까지 반복하고
        for j in range(a-1, -1, -1):        # a-1부터 0까지 반복해서
            ans += A[(a*(a-1)+i) - (j*a)]   # 해당 위치의 문자를 ans에 더한다
    else:                                   # 모든 반복이 끝났다면
        print(ans)                          # ans를 출력한다