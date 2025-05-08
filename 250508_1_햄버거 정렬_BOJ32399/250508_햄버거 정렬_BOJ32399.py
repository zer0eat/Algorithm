# 햄버거 정렬_BOJ32399

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = input().strip() # 햄버거의 상태를 input받고
if S == '(1)':      # 햄버거가 정상이라면
    print(0)        # 0을 출력하고
elif S == ')1(':    # 햄버거가 뒤집혀있다면
    print(2)        # 2를 출력하고
else:               # 그 외의 경우
    print(1)        # 1을 출력한다