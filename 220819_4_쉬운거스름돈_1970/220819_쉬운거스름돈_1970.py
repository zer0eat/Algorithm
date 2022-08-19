# 쉬운거스름돈_1970

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):
    N = int(input())                                # 거스름돈의 액수

    changes = [[0] for _ in range(8)]               # 거스름돈의 숫자를 적을 0이 적힌 리스트 만들기

    while N > 0:                                    # 거스름돈이 없을 때까지 반복
        if N >= 50000:                              # 거스름돈이 50000이상이면
            changes[0][0] += (N // 50000)           # 50000짜리 거스름돈의 개수를 changes의 0번째 인덱스에 추가한다
            N = N - 50000 * changes[0][0]           # 거스름돈의 총액 수에서 준 만큼 빼서 남은 액수 계산
        elif N >= 10000:                            # 거스름돈이 10000이상이면
            changes[1][0] += (N // 10000)           # 10000짜리 거스름돈의 개수를 changes의 1번째 인덱스에 추가한다
            N = N - 10000 * changes[1][0]           # 거스름돈의 총액 수에서 준 만큼 빼서 남은 액수 계산
        elif N >= 5000:                             # 거스름돈이 5000이상이면
            changes[2][0] += (N // 5000)            # 5000짜리 거스름돈의 개수를 changes의 2번째 인덱스에 추가한다
            N = N - 5000 * changes[2][0]            # 거스름돈의 총액 수에서 준 만큼 빼서 남은 액수 계산
        elif N >= 1000:                             # 거스름돈이 1000이상이면
            changes[3][0] += (N // 1000)            # 1000짜리 거스름돈의 개수를 changes의 3번째 인덱스에 추가한다
            N = N - 1000 * changes[3][0]            # 거스름돈의 총액 수에서 준 만큼 빼서 남은 액수 계산
        elif N >= 500:                              # 거스름돈이 500이상이면
            changes[4][0] += (N // 500)             # 500짜리 거스름돈의 개수를 changes의 4번째 인덱스에 추가한다
            N = N - 500 * changes[4][0]             # 거스름돈의 총액 수에서 준 만큼 빼서 남은 액수 계산
        elif N >= 100:                              # 거스름돈이 100이상이면
            changes[5][0] += (N // 100)             # 100짜리 거스름돈의 개수를 changes의 5번째 인덱스에 추가한다
            N = N - 100 * changes[5][0]             # 거스름돈의 총액 수에서 준 만큼 빼서 남은 액수 계산
        elif N >= 50:                               # 거스름돈이 50이상이면
            changes[6][0] += (N // 50)              # 50짜리 거스름돈의 개수를 changes의 6번째 인덱스에 추가한다
            N = N - 50 * changes[6][0]              # 거스름돈의 총액 수에서 준 만큼 빼서 남은 액수 계산
        elif N >= 10:                               # 거스름돈이 10이상이면
            changes[7][0] += (N // 10)              # 10짜리 거스름돈의 개수를 changes의 7번째 인덱스에 추가한다
            N = N - 10 * changes[7][0]              # 거스름돈의 총액 수에서 준 만큼 빼서 남은 액수 계산
        elif N < 10:                                # 1의 자리 이하는 절삭
            break

    print(f'#{t+1}')                                # 테스트 케이스를 출력하고
    lst = [change[0] for change in changes]         # 새로운 리스트에 int만 입력하고 출력한다
    print(*lst)
    # 다른 출력방법
    # print(*changes[0], *changes[1], *changes[2], *changes[3], *changes[4], *changes[5], *changes[6],*changes[7])
