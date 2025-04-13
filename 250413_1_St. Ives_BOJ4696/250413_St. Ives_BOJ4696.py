# St. Ives_BOJ4696

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                # 0이 나올때까지 반복해서
    N = float(input())                  # 와이프의 숫자를 input 받고
    if N == 0:                          # 0이 나왔다면 
        break                           # while문을 break한다
    print('%.2f'%(1+N+N**2+N**3+N**4))  # 와이프 자루 고양이 새끼고양이의 합을 출력한다