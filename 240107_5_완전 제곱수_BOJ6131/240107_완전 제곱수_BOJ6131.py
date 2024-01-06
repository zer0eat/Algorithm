# 완전 제곱수_BOJ6131

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # A와 B의 차이를 input받고
dic = dict()                # 제곱수를 저장할 딕셔너리를 생성한다
for i in range(1, 501):     # B를 반복해서
    dic[i**2] = 1           # B의 제곱수를 key로 저장하고
ans = 0                     # A보다 N개 큰 B의 수를 저장할 변수를 생성하고
for i in range(1, 501):     # A를 반복해서
    if dic.get(i**2 + N):   # A의 제곱수보다 N 큰 B의 제곱수가 있다면
        ans += 1            # ans에 1을 추가하고
print(ans)                  # A의 제곱수보다 N만큼 큰 B의 제곱수가 있는 경우의 수를 출력한다