# ZOAC 6_BOJ30045

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 문자의 수를 input받고
ans = 0                         # 정답을 저장할 변수를 생성해서
for n in range(N):              # 문자의 수를 반복해서
    S = input().strip()         # 문자를 input받고
    if '01' in S or 'OI' in S:  # 01이나 OI가 포함된다면
        ans += 1                # 정답을 추가하고
print(ans)                      # 이모티콘을 넣은 횟수를 출력한다