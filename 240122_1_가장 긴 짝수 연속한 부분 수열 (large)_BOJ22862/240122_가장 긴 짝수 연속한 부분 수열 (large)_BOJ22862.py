# 가장 긴 짝수 연속한 부분 수열 (large)_BOJ22862

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S, K = map(int, input().split())        # S 수열의 길이 / K 삭제할 수 있는 횟수를 input 받고
lst = list(map(int, input().split()))   # 수열 리스트를 input 받는다
ans = 0                                 # 최대 길이를 저장할 변수를 생성하고
l = 0                                   # 왼쪽 끝지점을 나타낼 포인터를 생성하고
r = 0                                   # 오른쪽 끝지점을 나타낼 포인터를 생성한다
cnt = 0                                 # 삭제한 원소의 수를 저장할 변수를 생성하고
while 1:                                # break가 나올때까지 반복해서
    if r == S:                          # 오른쪽 포인터가 S에 도달 했다면
        break                           # while문을 종료한다
    elif cnt > K:                       # 지운 원소의 수가 K개보다 많아졌다면
        if lst[l]%2:                    # 맨 앞의 원소가 홀수라면
            cnt -= 1                    # cnt를 1 줄이고
        l += 1                          # 왼쪽포인터를 한칸 이동시킨다
    else:                               # 지운 원소의 수가 K개 이하라면
        if lst[r]%2:                    # 맨 뒤의 원소가 홀수라면
            cnt += 1                    # cnt를 1 증가시키고
        r += 1                          # 오른쪽포인터를 한칸 이동시킨다
    if cnt <= K:                        # cnt가 K개 이하라면
        ans = max(ans, r-l-cnt)         # ans와 현재 길이 중 더 큰 값을 ans에 저장하고
print(ans)                              # 연속한 부분 수열의 길이 중 가장 큰 값을 출력한다