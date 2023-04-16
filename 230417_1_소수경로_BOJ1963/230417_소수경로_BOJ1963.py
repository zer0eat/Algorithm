# 에라토스테네스의 체_BOJ2960

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())        # N보다 작은 소수를 찾기 위한 기준 / K번째 지워지는 수
visited = [0]*(N+1)                     # 인덱스가 N까지 있는 리스트를 생성하고
cnt = 0                                 # 지워지는 순서를 셀 변수 생성
for i in range(2, N+1):                 # 2부터 N까지 반복해서
    if visited[i] == 0:                 # 해당 숫자가 방문 전이라면
        for j in range(i, N+1, i):      # 해당 숫자 i부터 N까지 i간격으로 반복해서
            if visited[j] == 0:         # 반복한 숫자 j가 방문전이라면
                visited[j] = 1          # 방문표시를  해주고
                cnt += 1                # cnt에 1을 추가한다
                if cnt == K:            # cnt가 K라면
                    print(j)            # j를 출력한다