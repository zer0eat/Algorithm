# 배열최소합_13882

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 최소합을 구하는 함수
def f(a, b):                                # a = 시작 값 / b = 부분 집합의 원소의 개수
    global mini                             # mini를 global로 선언
    if a == b:                              #
        if mini > sum(res[:b]):             #
            mini = sum(res[:b])             #
            # ans.append(res[:])
        # print(3, ans)
        return                              # 함수 종료
    for n in range(b):                      # 부분집합의 원소의 개수를 반복할 때
        if n not in bit[0:a]:               # n 이 bit[0:a]에 포함되지 않을 때
            bit[a] = n                      # n 으로 바꿈 (인덱스)
            # print(1, bit)
            res[a] = arr[a][n]              # arr[a][n]의 값을 추가 (인덱스에 해당하는 값)
            # print(2, res)
            if sum(res[:a]) > mini:         # 가지치기 / 만약 최소값보다 이미 크다면
                continue                    # 다음을 패스
            f(a+1, b)                       # 다음 값을 함수에 돌림

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):                          # 테스트 케이스 수만큼 반복
    N = int(input())                        # 행렬의 길이를 N으로 input
    arr = [list(map(int, input().split())) for n in range(N)]   # 길이가 N인 행렬을 arr에 input

    # print(arr)

    # 경우의 수 찾기
    bit = [0] * N                           # 비트 리스트를 행렬의 길이 만큼 만들고
    res = [0] * N                           # 결과를 담을 리스트를 행렬의 길이 만큼 만든다
    # ans = []

    mini = 10 * N                           # 나올 수 있는 최대 값으로 설정

    f(0, N)                                 # 함수를 돌린 후

    # for i in ans:
    #     ans = 0
    #     for j in i:
    #         ans += j
    #     else:
    #         if mini > ans:
    #             mini = ans

    print(f'#{t+1}', mini)                  # 최소값을 출력한다