# 상근이의 친구들_BOJ5717

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                # while문을 break가 나올때까지 반복해서
    M, F = map(int, input().split())    # 남자와 여자친구를 input 받고
    if (M, F) == (0, 0):                # 친구가 없다면
        break                           # while문을 break하고
    print(M+F)                          # 친구가 있다면 남자 여자를 합한 친구의 수를 출력한다