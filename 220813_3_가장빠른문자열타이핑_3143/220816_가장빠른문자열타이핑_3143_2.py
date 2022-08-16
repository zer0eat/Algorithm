# 가장 빠른 문자열 타이핑_3143_슬라이싱 없이

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스 개수
for t in range(T):
    A, B = input().split() # A 입력할 문자 B 저장한 문자

    length = len(A) # 타이핑할 문자열의 수
    a = 0 # 리스트 A의 인덱스
    while a < len(A) - len(B) + 1:

        # 타이핑할 문자와 저장한 문자의 첫글자가 같을 때
        if A[a] == B[0]:
            lst_s = ''

            # len(B)의 길이만큼 반복한 후
            for b in range(len(B)):
                lst_s += A[a+b]
            else:
                # 같으면 len(B)만큼 감소
                if lst_s == B:
                    length -= len(B) - 1
                    a += len(B)
                # 없으면 다음칸으로 이동
                elif lst_s != B:
                    a += 1

        # 타이핑할 문자와 저장한 문자의 첫글자가 다를 때 다음 문자로 이동
        elif A[a] != B[0]:
            a += 1

    print(f'#{t+1}', length)
