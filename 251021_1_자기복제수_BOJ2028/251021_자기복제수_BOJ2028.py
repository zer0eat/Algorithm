# 자기복제수_BOJ2028

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스를 input받고
for t in range(T):                          # 테스트 케이스를 반복해서
    N = int(input())                        # 숫자를 input 받고
    tmp = N**2                              # 숫자를 제곱해서
    if str(N) == str(tmp)[-len(str(N)):]:   # 마지막 N자리가 N과 같다면
        print('YES')                        # 자기복제수를 예를 출력하고
    else:                                   # 다르다면
        print('NO')                         # 자기복제수를 아니오로 출력한다