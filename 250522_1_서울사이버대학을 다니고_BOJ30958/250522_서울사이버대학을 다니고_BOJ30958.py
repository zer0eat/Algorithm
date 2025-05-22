# 서울사이버대학을 다니고_BOJ30958

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 문장의 길이를 input받고
song = input().strip()          # 문장을 input받고
ans = [0]*26                    # 정답을 저장할 리스트를 생성한다
for s in song:                  # 문장의 스펠링을 반복해서
    if s.isalpha():             # 영어라면
        ans[ord(s)-97] += 1     # 해당 스펠링의 수를 추가하고
print(max(ans))                 # 가장 많이 나온 수를 출력한다