# 특별한 학교 이름_BOJ27889

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = input().strip()                         # 약어를 input 받고
if N == 'NLCS':                             # NLCS라면
    print('North London Collegiate School') # North London Collegiate School를 출력한다 
elif N == 'BHA':                            # BHA 라면
    print('Branksome Hall Asia')            # Branksome Hall Asia를 출력한다
elif N == 'KIS':                            # KIS 라면
    print('Korea International School')     # Korea International School를 출력한다
elif N == 'SJA':                            # SJA 라면
    print('St. Johnsbury Academy')          # St. Johnsbury Academy를 출력한다