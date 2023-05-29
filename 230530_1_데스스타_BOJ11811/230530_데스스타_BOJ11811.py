# 데스스타_BOJ11811

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 행렬의 크기
lst = [list(map(int, input().split())) for _ in range(N)]   # 행렬의 크기를 input 받고

ans = [0] * N                                               # 정답을 저장할 리스트 생성
for i in range(N):                                          # 행을 반복하고
    for j in range(N):                                      # 열을 반복해서
        if i == j:                                          # 행 열이 같은 원소는
            continue                                        # continue한다
        ans[i] = max(ans[i], lst[i][j] | lst[j][i])         # ans의 i번째 원소에 ans[i]와 lst[i][j], lst[j][i] 비트연산 and 값 중 큰 값으로 저장한다

print(*ans)                                                 # ans를 출력한다