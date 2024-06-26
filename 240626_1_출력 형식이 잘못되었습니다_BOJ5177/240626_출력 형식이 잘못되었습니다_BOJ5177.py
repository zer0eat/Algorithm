# 출력 형식이 잘못되었습니다_BOJ5177

# input.txt 열기
import sys
import re
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def change(s):
    s = s.lower()                           # 소문자로 변환하고
    s = s.replace('(', '[')                 # 소괄호를 대괄호로 변환하고
    s = s.replace('{', '[')                 # 중괄호를 대괄호로 변환하고
    s = s.replace(')', ']')                 # 소괄호를 대괄호로 변환하고
    s = s.replace('}', ']')                 # 증괄호를 대괄호로 변환하고
    s = s.replace(',', ';')                 # ,를 ;으로 변환하고
    s = re.sub(r'\s*([\[\]\.,;:])\s*', r'\1', s)    # 괄호 앞뒤 띄어쓰기를 무시하고
    s = re.sub(r'\s+', ' ', s)              # 연속되는 띄어쓰기를 한개로 변환하고
    return s                                # 변환한 문자열을 return한다

K = int(input())                            # 테스트케이스를 input 받고
for k in range(1, K+1):                     # 테스트케이스를 반복해서
    s1 = input().strip()                    # s1 문자열을 input 받고
    s2 = input().strip()                    # s2 문자열을 input 받아서
    if change(s1) == change(s2):            # 두 문자열이 같다면
        print(f'Data Set {k}: equal')       # equal을 출력하고
    else:                                   # 두 문자열이 다름다면
        print(f'Data Set {k}: not equal')   # not equal을 출력하고
    if k != K:                              # 마지막 케이스가 아니라면
        print()                             # 한 줄을 건너뛴다