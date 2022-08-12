# 회문_13755

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 회문 찾는 함수 만들기
def palindrome(list):
    a = []
    for n in range(N):
        for m in range(M):
            if list[n][m] == list[n][M - m - 1] and list[n][m + 1] == list[n][M - m - 2]:
                a.append(list[n][m])
            if list[m][n] == list[M - m - 1][n] and list[m + 1][n] == list[M - m - 2][n]:
                a.append(list[m][n])
    return a

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N, M = map(int, input().split()) # 입력될 문장의 숫자


    lst = [] # 행렬로 입력된 문장
    for nn in range(N):
        lst.append(list(input()))

    print(palindrome(lst))









    # 회문 찾기
    # lst2 = [[0]*N for _ in range(N)]
    # for n in range(N):
    #     for m in range(N):
    #             lst2[n][m] = lst[m][n]
    #
    # print(lst2)
