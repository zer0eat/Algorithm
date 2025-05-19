# 학점계산프로그램_BOJ29614

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
grade = {
    'A+':4.5,
    'A':4.0,
    'B+':3.5,
    'B':3.0,
    'C+':2.5,
    'C':2.0,
    'D+':1.5,
    'D':1.0,
    'F':0.0
    }                               # 학점 딕셔너리를 만들고
ans = 0                             # 학점을 저장할 변수를 생성해서
S = list(input().strip())           # 학점을 input받고
s = len(S)                          # 학점의 길이를 저장하고
n = 0                               # 학점의 위치를 저장할 변수를 생성하고
m = 0                               # 학점의 수를 저장할 변수를 생성하고
while n < s:                        # 학점을 반복해서
    if n+1 < s and S[n+1] == '+':   # 마지막이 아니고 다음이 +라면
        tmp = S[n]+S[n+1]           # 학점을 변수에 저장하고
        n += 2                      # 학점의 위치를 2 옮기고
        m += 1                      # 학점의 수를 1 더한다
    else:                           # 마지막이거나 다음이 +가 아니라면
        tmp = S[n]                  # 학점을 변수에 저장하고
        n += 1                      # 학점의 위치를 1 옮기고
        m += 1                      # 학점의 수를 1 더한다
    ans += grade[tmp]               # 학점을 변수에 더하고
print(ans/m)                        # 학점의 평균을 출력한다