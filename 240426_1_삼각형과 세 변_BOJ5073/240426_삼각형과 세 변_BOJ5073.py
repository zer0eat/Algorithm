# 삼각형과 세 변_BOJ5073

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                    # break가 나올때까지 반복해서
    A = list(map(int, input().split()))     # 삼각형의 세 변을 리스트로 input 받고
    if A == [0, 0, 0]:                      # 세변이 0, 0, 0이라면
        break                               # while문을 종료한다
    else:                                   # 세변이 모두 0이 아니라면
        A.sort()                            # 오름차순으로 정렬하고
        if A[0] + A[1] <= A[2]:             # 두변의 합보다 한변이 같거나 크다면
            print('Invalid')                # Invalid를 출력하고
        elif A[0] == A[1] and A[1] == A[2]: # 모든 변이 같다면
            print('Equilateral')            # Equilateral를 출력하고
        elif A[0] == A[1] or A[1] == A[2]:  # 두변이 같고 나머지 한변이 다르다면
            print('Isosceles')              # Isosceles를 출력하고
        else:                               # 세변이 모두 다른 경우
            print('Scalene')                # Scalene을 출력한다