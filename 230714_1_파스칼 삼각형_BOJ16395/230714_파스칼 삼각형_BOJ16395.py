# 파스칼 삼각형_BOJ16395

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())                            # N 파스칼 삼각형의 행 / K N번째 줄의 원소 번호
pascal = []                                                 # 파스칼 삼각형의 원소를 저장할 리스트 생성
for i in range(1, N+1):                                     # 첫번째 줄부터 N번째 줄까지 반복해서
    tmp = []                                                # i번째 줄의 원소를 저장할 리스트를 생성하고
    for j in range(i):                                      # i개의 원소를 반복해서
        if j == 0 or j == i-1:                              # 0 또는 i-1의 인덱스의 원소라면
            tmp.append(1)                                   # tmp에 1을 append 하고
        else:                                               # 그 이외의 원소라면
            tmp.append(pascal[i-2][j-1] + pascal[i-2][j])   # 앞줄의 원소에서 j-1과 j번째 원소의 합을 append 한다
    pascal.append(tmp)                                      # i번째 원소를 모두 탐색했다면 tmp를 pascal에 append 한다
print(pascal[N-1][K-1])                                     # N번째 K원소를 출력한다