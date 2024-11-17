# 母音を数える (Counting Vowels)_BOJ18409

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 글자의 수를 input 받고
S = input().strip()                     # 글자를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
for s in S:                             # 글자를 반복해서
    if s in ['a', 'e', 'i', 'o' ,'u']:  # 글자의 스펠링이 모음이라면
        ans += 1                        # 정답에 1을 출력하고
print(ans)                              # 모음의 수를 출력한다