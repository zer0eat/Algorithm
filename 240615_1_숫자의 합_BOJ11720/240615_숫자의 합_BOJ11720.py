# 숫자의 합_BOJ11720

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 숫자의 개수를 input 받고
lst = list(input().strip())     # N개의 숫자를 input 받아서
ans = 0                         # 정답을 저장할 변수를 생성하고
for l in lst:                   # 숫자를 반복해서
    ans += int(l)               # 숫자를 변수에 더해준 후
print(ans)                      # N개의 숫자를 출력한다