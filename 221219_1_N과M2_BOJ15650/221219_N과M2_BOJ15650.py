# N과M2_BOJ15650

# import.txt 열기
import sys
sys.stdin = open('input.txt')

def choice(n):
    global N, M                                 # N과 M을 global로 불러오고
    if n == N:                                  # n이 N과 같아져 모든 bit를 확인했다면
        if sum(bit) == M:                       # bit의 합이 M인 경우에만
            ans = []                            # 정답을 담을 리스트 생성
            for b in range(len(bit)):           # bit를 반복해서
                if bit[b] == 1:                 # 해당 인덱스의 bit가 1인 경우에만
                    ans.append(lst[b])          # 해당 인덱스의 lst의 요소를 ans에 append
            else:                               # 반복이 끝났으면
                print(*ans)                     # ans를 출력한다
        return                                  # 리턴
    bit[n] = 1                                  # 인덱스 n의 비트를 1로 변경하고
    choice(n+1)                                 # choice 함수를 n+1을 넣고 실행
    bit[n] = 0                                  # 인덱스 n의 비트를 0으로 변경하고
    choice(n+1)                                 # choice 함수를 n+1을 넣고 실행
    return                                      # 리턴

# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 수열의 개수 / M 중복 없이 고를 개수
lst = [_ for _ in range(1,N+1)]                 # 1부터 N까지의 수열을 리스트로 생성
bit = [0]*N                                     # N개의 bit를 생성

choice(0)                                       # choice 함수를 실행

