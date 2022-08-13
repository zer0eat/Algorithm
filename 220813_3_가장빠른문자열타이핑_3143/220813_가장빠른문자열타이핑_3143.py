# 가장 빠른 문자열 타이핑_3143

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스 개수
for t in range(T):
    A, B = input().split() # A 입력할 문자 B 저장한 문자

    a = 0 # a = A의 인덱스
    cnt = 0 # 입력한 숫자
    while a < len(A):
        # 만약 B가 있다면 입력할 숫자 1 더하고 입력한 만큼 건너 뛰기
        if A[a : a+len(B)] == B:
            cnt += 1
            a = a + len(B)
        # 만약 B가 없다면 입력할 숫자 1 더하고 다음으로 넘어가기
        elif A[a : a+len(B)] != B:
            cnt += 1
            a += 1

    print(f'#{t+1} {cnt}')
