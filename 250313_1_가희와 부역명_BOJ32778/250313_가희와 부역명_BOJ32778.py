# 가희와 부역명_BOJ32778

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
name = input().strip()          # 역 이름을 input 받고
if '(' in name:                 # 이름에 (가 들어가면
    s, e = name.index('('), name.index(')') # 괄호의 순서를 구해서
    print(name[: s - 1])        # 역 이름과
    print(name[s + 1 : e])      # 부역 이름을 출력하고
else:                           # 부역명이 없다면
    print(name)                 # 역 이름을 출력하고
    print('-')                  # -를 출력한다