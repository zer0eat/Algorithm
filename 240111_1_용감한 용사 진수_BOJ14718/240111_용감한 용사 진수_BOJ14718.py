# 용감한 용사 진수_BOJ14718

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())                                # N 병사의 수 / K 이겨야할 병사의 수
ans = 1e9                                                       # 최소 스탯포인트를 저장할 변수를 생성하고
warrior = [list(map(int, input().split())) for _ in range(N)]   # 병사의 스탯을 리스트로 input 받고
for i in range(N):                                              # 병사의 힘을 반복하고
    for j in range(N):                                          # 병사의 민첩을 반복하고
        for k in range(N):                                      # 병사의 지능을 반복해서
            cnt = 0                                             # 이길 수 있는 병사의 수를 저장할 변수를 생성하고
            for n in range(N):                                  # 병사의 수를 반복해서
                if warrior[i][0] >= warrior[n][0] and warrior[j][1] >= warrior[n][1] and warrior[k][2] >= warrior[n][2]:    # n번째 병사가 현재 진수의 스탯보다 낮다면
                    cnt += 1                                    # 이길수 있는 병사의 수에 1추가하고
                if cnt >= K:                                    # 이길 수 있는 병사의 수가 K명 이상이라면
                    ans = min(ans, warrior[i][0] + warrior[j][1] + warrior[k][2])                                           # 진수의 최소 스탯과 현재 스탯 중 낮은 값으로 저장한다
print(ans)                                                      # K명을 이길 수 있는 최소스탯을 출력한다