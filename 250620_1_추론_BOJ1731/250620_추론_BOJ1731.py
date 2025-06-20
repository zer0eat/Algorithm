# 추론_BOJ1731

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 숫자의 수를 input받고
ans = []                            # 정답을 저장할 리스트를 생성해서
for n in range(N):                  # 숫자의 수를 반복해서
    ans.append(int(input()))        # 리스트에 저장한다
tmp = 0                             # 등비 등차를 저장할 변수를 생성하고
if ans[1]-ans[0] == ans[2]-ans[1]:  # 등차 수열이라고 하면
    Q = ans[1]-ans[0]               # 그 차이를 저장하고
else:                               # 등비 수열이라고 하면
    Q = ans[1]//ans[0]              # 그 비율을 저장하고
    tmp = 1                         # 등비 수열 표시를 한다
if tmp:                             # 등비 수열이라면 
    print(ans[-1]*Q)                # 마지막 수에 등비를 곱해 정답을 출력하고
else:                               # 등차 수열이라면
    print(ans[-1]+Q)                # 마지막 수에 등차를 더해 정답을 출력한다