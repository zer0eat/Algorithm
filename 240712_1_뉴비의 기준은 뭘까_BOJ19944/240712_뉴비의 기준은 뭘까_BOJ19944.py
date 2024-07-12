# 뉴비의 기준은 뭘까_BOJ19944

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # N학년과 M학년을 input 받고
if N >= M and M in [1, 2]:          # N학년 이하이면서 1,2 학년이라면
    print('NEWBIE!')                # 뉴비를 출력하고
elif N >= M and M not in [1, 2]:    # N학년 이하이지만 3학년 이상이라면
    print('OLDBIE!')                # 올드비를 출력하고
else:                               # 둘다 아니라면
    print('TLE!')                   # TLE를 출력한다