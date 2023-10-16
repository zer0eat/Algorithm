# 소수_BOJ1312

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, N = map(int, input().split())     # A 분자 / B 분모 / N 소수점 자리수를 input 받고
ans = []                                # 소수점 각 자리를 몫을 저장할 리스트를 생성하고
A = A%B                                 # A에서 B를 나눈 나머지를 A에 저장한다
for i in range(N):                      # 소수 N번째 자리까지 반복해서
    ans.append((A*10)//B)               # 소수 i번째자리의 몫을 ans에 append하고
    A = (A*10) % B                      # 소수 i번째자리까지 구하고 난 나머지를 A에 저장한다
print(ans[-1])                          # 소수 N번째 자리의 수를 출력한다