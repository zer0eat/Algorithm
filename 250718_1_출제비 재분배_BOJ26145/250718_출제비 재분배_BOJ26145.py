# 출제비 재분배_BOJ26145

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())            # 출제자와 검수자를 input받고
S = list(map(int, input().split()))         # 출제비를 리스트로 input받고
ans = S + [0]*M                             # 정답을 저장할 리스트를 생성한다
for i in range(N):                          # 출제자를 반복하고
    money = list(map(int, input().split())) # 출제자가 다른사람에게 줄 돈을 리스트로 input받고
    for j in range(N+M):                    # 출제자와 검수자를 반복해서
        ans[i] -= money[j]                  # i가 j번째 사람에게 줄 돈을 i에게서 빼고
        ans[j] += money[j]                  # j가 받을 돈을 더해준다
print(*ans)                                 # 출제자와 검수자가 받은 돈을 출력한다