# 나는 친구가 적다 (Large)_BOJ16172

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = tuple(input())      # 교과서를 input 받고
K = input().strip()     # 정답을 input 받고
ans = list()            # 정답을 저장할 리스트를 생성하고
for s in S:             # 교과서를 반복해서
    if s.isalpha():     # 교과서의 글씨가 숫자가 아니라면
        ans.append(s)   # 리스트에 글씨를 append한다
ans = ''.join(ans)      # 리스트를 붙여서 하나의 문자열로 만들고
if K in ans:            # K가 ans 안에 존재하면
    print(1)            # 1을 출력하고
else:                   # K가 ans 안에 없다면
    print(0)            # 0을 출력한다