# 팬덤이 넘쳐흘러_BOJ17262

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 학생의 수를 input 받고
S = []                                  # 등교시간을 저장할 리스트를 생성하고
E = []                                  # 하교시간을 저장할 리스트를 생성한다
for n in range(N):                      # N명의 학생을 반복해서
    s, e = map(int, input().split())    # 등하교 시간을 input 받고
    S.append(s)                         # S에 등교시간을 append하고
    E.append(e)                         # E에 하교시간을 append한다
S.sort()                                # 등교시간을 오름차순 정렬하고
E.sort()                                # 하교시간을 오름차순 정렬해서
if S[-1]-E[0] <= 0:                     # 가장 늦게 등교한 사람이 가장 처음 하교한 사람보다 빠르다면
    print(0)                            # 0을 출력하고
else:                                   # 가장 늦게 등교한 사람이 가장 처음 하교한 사람보다 느리다면
    print(S[-1]-E[0])                   # 그 사이 시간을 출력한다