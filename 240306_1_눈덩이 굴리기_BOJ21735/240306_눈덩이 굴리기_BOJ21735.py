# 눈덩이 굴리기_BOJ21735

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                    # N 앞마당의 길이 / M 대회의 시간을 input 받고
A = list(map(int, input().split()))                 # 마당에 있는 눈의 크기를 리스트로 input 받는다
ans = 0                                             # 정답을 저장할 변수를

def recur(dep, start, snow):
    global ans                                      # ans를 global 변수로 선언하고
    ans = max(ans, snow)                            # ans에 현재 눈덩이와 ans 중 더 큰 값을 저장한다
    if dep == M:                                    # 시간이 모두 지났다면
        return                                      # return하고
    if start >= N:                                  # 마당의 길이를 넘어 섰다면
        return                                      # reuturn한다
    recur(dep+1, start+1, snow+A[start])            # 눈덩이를 굴렸을 때 크기를 탐색하고
    if start < N-1:                                 # 점프를 할 수 있는 마당이 남았다면
        recur(dep+1, start+2, snow//2+A[start+1])   # 눈덩이를 던졌을 때 크기를 탐색한다

recur(0, 0, 1)                                      # 0초에서 눈덩이의 크기를 탐색해서
print(ans)                                          # 시간 내에 가장 크게 만들 수 있는 눈덩이의 크기를 출력한다