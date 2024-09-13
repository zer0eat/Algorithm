# 성택이의 은밀한 비밀번호_BOJ25372

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 비밀번호의 수를 input 받고
for n in range(N):                      # 비밀번호의 수를 반복해서
    pw = input().strip()                # 비밀번호를 input 받고
    if len(pw) <= 9 and len(pw) >= 6:   # 비밀번호가 6~9자리라면
        print('yes')                    # yes를 출력하고
    else:                               # 아니라면
        print('no')                     # no를 출력한다