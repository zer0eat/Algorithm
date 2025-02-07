# 3 つの整数 (Three Integers)_BOJ18408

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = [0, 0]                                # 정답을 저장할 리스트를 생성하고
for a in list(map(int, input().split())):   # 숫자 리스트를 input 받아 반복해서
    ans[a-1] += 1                           # 숫자의 수를 더해주고
if ans[0] < ans[1]:                         # 2가 더 많다면
    print(2)                                # 2를 출력하고
else:                                       # 1이 더 많다면
    print(1)                                # 1을 출력한다