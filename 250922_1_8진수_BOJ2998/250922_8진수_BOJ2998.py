# 8진수_BOJ2998

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
E = input().strip()                 # 2진수를 input받고
ans = 0                             # 10진수를 저장할 변수를 생성하고
tmp = 1                             # 2진수를 나타낼 변수를 생성하고
for n in range(len(E)-1,-1,-1):     # 2진수를 뒤에서부터 반복해서
    ans += tmp * int(E[n])          # 정답에 10진수로 변환해서 저장하고
    tmp *= 2                        # 2진수를 다음 단계로 넘어간다
print(oct(ans)[2:])                 # 10진수를 8진수로 변경하여 출력한다