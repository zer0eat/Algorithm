# 제로_BOJ10773

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
K = int(input())            # 숫자호출의 횟수를 K에 저장
ans = []                    # 정답을 저장할 빈 리스트 생성
for k in range(K):          # K번 반복할 때
    a = int(input())        # input을 int 형태로 a에 저장하고
    if a != 0:              # 0이 아닐때는
        ans.append(a)       # ans에 append
    else:                   # 0일 때는
        ans.pop()           # ans에서 마지막에 append 한것을 pop한다
print(sum(ans))