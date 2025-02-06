# 멀티탭 충분하니_BOJ15780

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())    # 사람과 멀티탭의 수를 input 받고
A = list(map(int, input().split())) # 멀티탭의 콘센트 수를 input 받고
socket = 0                          # 꽂을 수 있는 콘센트를 셀 변수를 생성하고
for a in A:                         # 콘센트의 수를 반복해서
    if a%2:                         # 멀티탭이 홀수라면
        socket += a//2+1            # 콘센트의 수를 2로 나눈 후 1을 더한 값을 추가하고
    else:                           # 멀티탭이 짝수라면
        socket += a//2              # 콘센트의 수를 2로 나눈 값을 추가한다
if N <= socket:                     # 모든 사람이 콘센트를 꽂을 수 있으면
    print('YES')                    # YES를 출력하고
else:                               # 모든 사람이 콘센트를 꽂을 수 없다면
    print('NO')                     # NO를 출력한다