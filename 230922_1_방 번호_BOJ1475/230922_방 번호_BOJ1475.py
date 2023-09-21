# 방 번호_BOJ1475

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
N = int(input())                    # 방번호를 input받고
ans = [0]*9                         # 방번호를 만들 숫자를 셀 리스트를 생성하고
for i in str(N):                    # 방번호를 반복해서
    if i == '9':                    # 번호가 9라면
        ans[6] += 1                 # 6에 1을 더하고
    else:                           # 번호가 6이 아니라면
        ans[int(i)] += 1            # 해당 숫자에 1을 더한다
else:                               # 방번호를 모두 탐색한 후
    ans[6] = math.ceil(ans[6]/2)    # 6의 개수를 2로 나누고 소수점은 올림한다
print(max(ans))                     # 필요한 세트의 개수를 출력한다
