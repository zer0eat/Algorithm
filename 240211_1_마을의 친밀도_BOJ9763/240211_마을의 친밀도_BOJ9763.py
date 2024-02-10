# 마을의 친밀도_BOJ9763

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 마을의 수를 input 받고
home = [list(map(int, input().split())) for _ in range(N)]  # 마을의 좌표를 리스트로 input 받는다
ans = 1e9                                                   # 정답을 저장할 변수를 생성하고
for i in range(N):                                          # 마을을 반복하고
    for j in range(N):                                      # 다른 마을을 반복해서
        if i != j:                                          # i와 j 마을이 다를 때
            tmp = abs(home[i][0] - home[j][0]) + abs(home[i][1] - home[j][1]) + abs(home[i][2] - home[j][2])                    # 두 마을의 친밀도를 tmp에 저장한다
            if ans > tmp:                                   # ans보다 tmp가 작을 때
                for k in range(N):                          # 마을을 반복해서
                    if i != k and j != k:                   # i,j와 다른 k일 때만
                        tmp2 = tmp + abs(home[k][0] - home[j][0]) + abs(home[k][1] - home[j][1]) + abs(home[k][2] - home[j][2]) # tmp2에 tmp와 j, k의 친밀도를 더한 값을 저장한다
                        ans = min(tmp2, ans)                # tmp2와 ans 중 더 작은 값을 저장한다
print(ans)                                                  # 세 마을의 친밀도 중 가장 작은 값을 출력한다