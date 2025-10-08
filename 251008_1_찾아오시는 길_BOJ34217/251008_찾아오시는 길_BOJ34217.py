# 찾아오시는 길_BOJ34217

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 역까지의 시간을 input받고
C, D = map(int, input().split())    # 학교까지의 시간을 input받고
H, Y = A+C, B+D                     # 집부터 학교까지 시간을 구해서
if H > Y:                           # 용답역이 빠르다면
    print('Yongdap')                # 용답을 출력하고
elif H < Y:                         # 한양대역이 빠르다면
    print('Hanyang Univ.')          # 한양대를 출력하고
else:                               # 시간이 같다면
    print('Either')                 # 같다고 출력한다