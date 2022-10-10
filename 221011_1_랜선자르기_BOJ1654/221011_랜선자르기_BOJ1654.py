# 랜선자르기_BOJ1654

# # input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
K, N = map(int, sys.stdin.readline().split())   # 랜선의 개수 K, 필요한 랜선의 개수 N

ans = []                                        # 랜선을 저장할 빈리스트 생성
for k in range(K):                              # 랜선의 수만큼 반복해서
    ans.append(int(sys.stdin.readline()))       # 랜선을 ans에 append

start = 1                                       # 랜선의 최소길이를 1로 저장하고
end = sum(ans) // N                             # 랜선의 최대길이를 전체길이를 N으로 나눈 것으로 설정한 후

while start <= end:                             # start가 end보다 커질때까지 반복해서
    middle = (start + end) // 2                 # middle을 start와 end의 합을 2로 나눈 몫으로 설정한다
    cnt = 0                                     # 잘린 랜선의 개수를 저장할 변수를 생성하고
    for a in ans:                               # 가지고 있는 랜선을 반복해서
        cnt += a // middle                      # cnt에 middle의 길이로 자른 몫을 더하고
    else:                                       # 모든 랜선을 반복했으면
        if cnt < N:                             # cnt가 필요한 랜선보다 작으면
            end = middle - 1                    # 끝점을 middle -1로 변경
        elif cnt >= N:                          # cnt가 필요한 랜선보다 많거나 같다면
            start = middle + 1                  # 시작점을 middle +1 로 변경

print(end)