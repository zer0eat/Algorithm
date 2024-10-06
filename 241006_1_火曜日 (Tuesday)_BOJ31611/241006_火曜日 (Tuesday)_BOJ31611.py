# 火曜日 (Tuesday)_BOJ31611

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X = int(input())    # X일 후를 input 받고
ans = X % 7         # X를 7로 나눈 나머지를 저장해서
if ans == 2:        # X일 후가 화요일이라면
    print(1)        # 1일 출력하고
else:               # X일 후가 화요일이 아니라면
    print(0)        # 0을 출력한다