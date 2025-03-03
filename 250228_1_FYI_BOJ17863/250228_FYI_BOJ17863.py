# FYI_BOJ17863

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = list(input().strip())   # 숫자를 input 받고
for n in range(3):          # 앞자리를 반복해서
    if N[n] == '5':         # 앞자리가 5라면
        pass                # 넘어가고
    else:                   # 5가 아니라면
        print('NO')         # NO를 출력하고
        quit()              # 종료한다
print('YES')                # 앞자리가 모두 5라면 YES를 출력한다