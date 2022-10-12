# 1,2,3 더하기_BOJ9095

# input.txt 열기
import sys

# input 받기
T = int(sys.stdin.readline())                   # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복해서
    a = [1, 2, 4]                               # 정답을 답을 리스트를 만들고
    N = int(sys.stdin.readline())               # 찾고자하는 정수를 N에 저장하고
    if N > 3:                                   # 3 초과라면
        for n in range(3,N):                    # 앞에 세 정수의 경우의 수의 합이 되므로
            a.append(a[n-1]+a[n-2]+a[n-3])      # 세 정수의 경우의수의 합을 a에 append
        else:                                   # 반복을 모두 마쳤다면
            print(a[-1])                        # 마지막에 넣은 숫자를 출력
    else:                                       # 3이하라면
        print(a[N-1])                           # a에 저장된 숫자 중 맞는 숫자를 출력한다