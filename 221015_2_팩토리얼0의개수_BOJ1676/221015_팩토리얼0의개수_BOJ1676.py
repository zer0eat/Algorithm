# 팩토리얼0의개수_BOJ1676

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())           # 팩토리얼을 구할 정수를 input 받음

ans = 1                                 # 정답을 저장할 변수를 생성하고
for n in range(1, N+1):                 # 1부터 N까지 반복해서
    ans *= n                            # ans에 곱해준 후

ans = str(ans)                          # str로 변경한다

cnt = 0                                 # 0이나올때마다 카운트할 변수를 생성하고
for c in range(len(ans)-1, -1, -1):     # 맨 뒤에서 부터 반복해서
    if ans[c] == '0':                   # 0이 나오면
        cnt += 1                        # cnt에 1을 추가하고
    else:                               # 0아 나오지 않으면 break
        break

print(cnt)