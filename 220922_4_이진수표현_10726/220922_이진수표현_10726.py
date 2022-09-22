# 이진수표현_10726

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def binary(a, N):                       # 이진수로 바꿔주기 위한 함수
    for i in range(N):                  # 뒤에서 N번째까지 확인할 때
        A = a % 2                       # 2로 나눈 나머지를 A에 저장하고
        a = a // 2                      # 2로 나눈 몫을 a로 바꿔준 후
        if A == 1:                      # A가 1일 때
            pass                        # 패스
        else:                           # 0이나오면
            return 'OFF'                # OFF를 리턴
    else:                               # 반복을 모두 마쳤다면 확인하는 구간이 모두 1이므로
        return 'ON'                     # ON을 리턴

# input 받기
T = int(input())                        # 테스트 케이스
for t in range(T):                      # 테스트 케이스를 반복할 때
    N, M = map(int, input().split())    # N = 이진수 표현에서 확인할 자리수  / M = 이진수로 바꿀 숫자

    print(f'#{t+1}', binary(M, N))      # 함수의 결과를 출력한다
