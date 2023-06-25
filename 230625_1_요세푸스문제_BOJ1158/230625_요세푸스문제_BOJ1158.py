# 요세푸스문제_BOJ1158

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())        # N 사람의 수 / K 제거하는 사람의 순서
lst = [i for i in range(1, N+1)]        # 사람을 리스트로 생성하고
visited = [0] * N                       # 방문표시를 할 리스트를 생성한다
cnt = 0                                 # K명을 셀 변수를 생성하고
idx = -1                                # 사람을 가르킬 포인터를 생성한다
ans = []                                # 정답을 저장할 리스트를 생성한 뒤
while len(ans) < N:                     # ans가 N이 될때까지 반복해서
    idx += 1                            # 포인터를 1 증가시키고
    if idx >= N:                        # 포인터가 N이상이 된 경우
        idx -= N                        # 포인터에서 N을 빼주고
    if visited[idx] == 0:               # 해당 포인터가 방문 전이라면
        cnt += 1                        # cnt에 1을 추가한다
        if cnt == K:                    # cnt가 K가 되어 K번째 사람을 가르킨다면
            cnt = 0                     # cnt를 초기화하고
            visited[idx] = 1            # 해당 사람을 방문표시한 후
            ans.append(lst[idx])        # ans에 해당 사람을 append 한다

print('<', end='')                      # < 를 출력하고
for a in range(N):                      # 정답을 반복해서
    if a == N-1:                        # 마지막 원소는
        print(ans[a], end='')           # 정답 출력 후 띄어쓰기 없이 출력하고
    else:                               # 나머지 원소는
        print(ans[a], end=', ')         # 정답 출력 후 , 를 출력한다
else:                                   # 모든 정답을 출력했다면
    print('>')                          # > 를 출력한다