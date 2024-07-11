# 히든 넘버_BOJ8595

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 히든넘버가 숨겨있는 문자열의 길이를 input 받고
h = list(input().strip())   # 문자열을 리스트로 input 받고
ans = 0                     # 정답을 저장할 변수를 생성하고
tmp = '0'                   # 히든넘버를 저장할 변수를 생성한다
for n in range(N):          # 문자열의 길이를 반복해서
    if h[n].isdigit():      # n번째 원소가 숫자라면
        tmp += h[n]         # 히든넘버에 더해주고
    else:                   # n번째 원소가 문자라면
        ans += int(tmp)     # 히든넘버를 정답에 더해주고
        tmp = '0'           # 히든넘버를 초기화한 후
else:                       # 모든 문자열을 반복했다면
    ans += int(tmp)         # 히든넘버를 정답에 더해주고
print(ans)                  # 모든 히든넘버의 합을 출력한다