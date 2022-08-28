# 줄세우기_BOJ2605

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                                # 학생 수
students = list(map(int, input().split()))      # 학생이 뽑은 카드 번호

line = []                                       # 급식을 받기 위한 줄

# 학생 줄세우기
for n in range(1, N+1):                         # 학생 수만큼 반복할 때
    if students[n - 1] == 0:                    # 0번 카드를 뽑았으면
        line.append(n)                          # 맨 뒤에 추가
    else:                                       # 0 이상의 카드를 뽑았다면
        line.insert(-students[n - 1], n)        # 숫자만큼 앞으로 와서 줄을 선다

print(*line)

