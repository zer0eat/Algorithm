# 집합_BOJ11723

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                   # 수행해야하는 연산의 수

S = set()                                       # 빈 set을 하나 만들고
for n in range(N):                              # 수행해야하는 연산을 반복해서
    A = list(sys.stdin.readline().split())      # A에 list형태로 input
    if A[0] == 'add':                           # 맨 앞 요소가 add일 때
        S.add(int(A[1]))                        # 두번째 요소를 더한다
    elif A[0] == 'remove':                      # 맨 앞 요소가 remove일 때
        try:                                    # S에 두번째 요소가 있으면
            S.remove(int(A[1]))                 # S에서 삭제한다
        except:                                 # S에 두번째 요소가 없으면 지나간다
            pass
    elif A[0] == 'check':                       # 맨 앞 요소가 check일 때
        if int(A[1]) in S:                      # 두번째 요소가 S에 있으면
            print(1)                            # 1을 출력
        else:                                   # 두번째 요소가 S에 없으면
            print(0)                            # 0을 출력
    elif A[0] == 'toggle':                      # 맨 앞 요소가 toggle일 때
        if int(A[1]) in S:                      # 두번째 요소가 S에 있으면
            S.remove(int(A[1]))                 # 지우고
        else:                                   # 두번째 요소가 S에 없으면
            S.add(int(A[1]))                    # 더한다
    elif A[0] == 'all':                         # 맨 앞 요소가 all일 때
        S = set([i for i in range(1,21)])       # S에 1부터 20까지 저장한다
    elif A[0] == 'empty':                       # 맨 앞 요소가 empty일 때
        S = set()                               # S를 비운다

