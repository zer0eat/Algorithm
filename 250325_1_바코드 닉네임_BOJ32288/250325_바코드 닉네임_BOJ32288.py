# 바코드 닉네임_BOJ32288

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 문자의 길이를 input 받고
ans = ''            # 정답을 저장할 변수를 생성한다
S = input().strip() # 문자를 input 받고
for s in S:         # 문자를 반복해서
    if s == 'l':    # l이면 
        ans += 'L'  # 대문자로 변경해서 저장하고
    else:           # I라면
        ans += 'i'  # 소문자로 변경해서 저장해서
print(ans)          # 정답을 출력한다