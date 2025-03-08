# 준살 프로그래밍 대회_BOJ7513

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                # 테스트 케이스를 input 받고
for t in range(T):                              # 테스트 케이스를 반복해서
    print(f'Scenario #{t+1}:')                  # 시나리오를 출력하고
    M = int(input())                            # 비밀번호의 부분 수를 input 받고
    lst = [input().strip() for _ in range(M)]   # 비밀번호의 부분을 리스트로 input받고
    N = int(input())                            # 추출할 비밀번호의 수를 input 받고
    for n in range(N):                          # 비밀번호의 수를 반복해서
        A = list(map(int, input().split()))     # 비밀번호 조합을 input 받고
        for a in range(A[0]):                   # 비밀번호의 길이를 반복해서
            print(lst[A[a+1]], end='')          # 비밀번호를 붙여서 출력하고
        else:                                   # 비밀번호를 완성했다면
            print()                             # 다음줄로 넘어가고
    else:                                       # 비밀번호를 모두 찾았다면
        print()                                 # 다음줄로 넘어간다