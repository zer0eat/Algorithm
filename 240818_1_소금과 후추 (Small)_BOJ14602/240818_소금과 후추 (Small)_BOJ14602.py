# 소금과 후추 (Small)_BOJ14602

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
M, N, K, W = map(int, input().split())                              # M 행의크기 / N 열의 크기 / 밝기 최대값 / W 픽셀의 크기를 input 받고
salt_pepper = [list(map(int, input().split())) for _ in range(M)]   # 소금과 후추의 사진을 리스트로 input 받는다
ans = [[0]*(N-W+1) for _ in range(M-W+1)]                           # 정답을 저장할 리스트를 생성하고
for i in range(M-W+1):                                              # 픽셀의 시작점의 행을 반복하고
    for j in range(N-W+1):                                          # 픽셀의 시작점의 열을 반복해서
        tmp = []                                                    # 픽셀 내 밝기를 저장할 리스트를 생성하고
        for x in range(W):                                          # 픽셀의 행을 반복하고
            for y in range(W):                                      # 픽셀의 열을 반복해서
                tmp.append(salt_pepper[i+x][j+y])                   # 픽셀 내 밝기를 tmp에 append한다
        else:                                                       # 픽셀의 밝기를 모두 리스트에 담았다면
            tmp.sort()                                              # 오름차순으로 정렬해서
            ans[i][j] = tmp[len(tmp)//2]                            # 중앙값을 정답 리스트에 저장한다
for a in ans:                                                       # 정답리스트를 반복해서
    print(*a)                                                       # 정답을 행렬로 출력한다