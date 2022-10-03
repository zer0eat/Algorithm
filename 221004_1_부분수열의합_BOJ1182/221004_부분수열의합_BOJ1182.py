# 부분수열의합_BOJ1182

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def on(a):
    global cnt, tmp
    if a == N:                                              # 비트를 모두 결정했을 때
        if sum(bit) == 0:                                   # 부분집합이 공집합이면
            return                                          # 리턴
        elif tmp == S:                                      # 공집합이 아닐때 tmp가 S인 경우
            cnt += 1                                        # cnt를 1 추가하고 리턴
        return

    bit[a] = 0                                              # 비트를 0으로 저장하고
    on(a+1)                                                 # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다
    bit[a] = 1                                              # 비트를 1로 저장하고
    tmp += arr[a]                                           # 부분집합에 포함 된 원소를 더한다
    on(a + 1)                                               # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다
    tmp -= arr[a]                                           # 부분집합에 포함 했던 원소를 뺀다

# input 받기
N, S = map(int, sys.stdin.readline().split())               # N 수열 / S 부분수열의 합
arr = list(map(int, sys.stdin.readline().split()))          # 수열을 리스트에 input

bit = [0]*N                                                 # 부분집합을 만들기 위한 비트 생성
cnt = 0                                                     # 부분집합의 합이 S가 되는 개수를 세기 위한 변수 생성
tmp = 0                                                     # 임시 저장값으로 사용할 변수를 생성

on(0)                                                       # 맨 앞 비트부터 순서대로 부분집합 생성성print(cnt)
print(cnt)