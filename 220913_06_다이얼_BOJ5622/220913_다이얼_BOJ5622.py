# 다이얼_BOJ5622

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
num = input()                                                   # 문자 받기
time = 0                                                        # 전화를 걸 때 걸리는 시간을 저장할 변수
for n in num:                                                   # 문자를 반복할 때
    if n == 'A' or n == 'B' or n == 'C':                        # A,B,C가 나오면 3초를 추가
        time += 3
    elif n == 'D' or n == 'E' or n == 'F':                      # D,E,F가 나오면 4초를 추가
        time += 4
    elif n == 'G' or n == 'H' or n == 'I':                      # G,H,I가 나오면 5초를 추가
        time += 5
    elif n == 'J' or n == 'K' or n == 'L':                      # J,K,L가 나오면 6초를 추가
        time += 6
    elif n == 'M' or n == 'N' or n == 'O':                      # M,N,O가 나오면 7초를 추가
        time += 7
    elif n == 'P' or n == 'Q' or n == 'R' or n == 'S':          # P,Q,R,S가 나오면 8초를 추가
        time += 8
    elif n == 'T' or n == 'U' or n == 'V':                      # T,U,V가 나오면 9초를 추가
        time += 9
    elif n == 'W' or n == 'X' or n == 'Y' or n == 'Z':          # W,X,Y,Z가 나오면 10초를 추가
        time += 10
print(time)
