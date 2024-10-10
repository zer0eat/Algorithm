# 골뱅이 찍기 - 돌아간 ㅈ_BOJ23809

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 셀의 크기를 input 받고
for n in range(N):              # 셀의 크기를 반복해서
    print('@'*N+'   '*N+'@'*N)  # 첫번째 줄을 출력하고
for n in range(N):              # 셀의 크기를 반복해서
    print('@'*N+'  '*N+'@'*N)   # 두번째 줄을 출력하고
for n in range(N):              # 셀의 크기를 반복해서
    print('@@@'*N)              # 세번째 줄을 출력하고
for n in range(N):              # 셀의 크기를 반복해서
    print('@'*N+'  '*N+'@'*N)   # 네번째 줄을 출력하고
for n in range(N):              # 셀의 크기를 반복해서
    print('@'*N+'   '*N+'@'*N)  # 다섯번째 줄을 출력한다