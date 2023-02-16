# 부울행렬의부울곱_BOJ14492

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                                   # 행렬의 크기
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # N*N 행렬을 A에 저장
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # N*N 행렬을 B에 저장
ans = 0                                                                 # 1의 개수를 셀 변수를 생성하고
for i in range(N):                                                      # A의 행을 반복하고
    for j in range(N):                                                  # B의 열을 반복하고
        for t in range(N):                                              # A의 열과 B의 행을 반복해서
            if A[i][t] * B[t][j] == 1:                                  # A[i][t] 와 B[t][j]가 1이면
                ans += 1                                                # ans에 1을 추가하고
                break                                                   # 더이상 계산해도 결과가 1로 변하지 않으므로 for문을 종료한다
print(ans)                                                              # 모든 반복을 마쳤다면 ans를 출력한다