# 요다_BOJ 5363

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                    # 문장의 수를 input받고
for n in range(N):                  # 문장의 수를 반복해서
    yoda = deque(input().split())   # 문장을 deque로 input받고
    for a in range(2):              # 맨 앞 두 단어를 반복해서
        yoda.append(yoda.popleft()) # 맨뒤로 넣어준다
    print(*yoda)                    # yoda가 말하는 말로 출력한다