# 과 조사하기_BOJ28289

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
P = int(input())            # 학생 수를 input 받고
ans = [0]*4                 # 정답을 저장할 변수를 생성해서
for p in range(P):          # 학생 수를 반복하고
    G, C, N = map(int, input().split()) # 학년 반 번호를 input 받고
    if G == 1:              # 1학년이라면
        ans[3] += 1         # 과가 없음으로 추가하고
    else:                   # 1학년이 아니라면
        if C in [1, 2]:     # 1,2반인 경우
            ans[0] += 1     # 소프트웨어개발과로 추가하고
        elif C == 3:        # 3반인 경우
            ans[1] += 1     # 임베디드소프트웨어개발과로 추가하고
        elif C == 4:        # 4반인 경우
            ans[2] += 1     # 인공지능소프트웨어개발과로 추가하고
for a in ans:               # 반별 인원을 반복해서
    print(a)                # 정답을 출력한다