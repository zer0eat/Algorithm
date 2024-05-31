# 전자레인지_BOJ14470

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())            # 고기의 온도를 input 받고
B = int(input())            # 목표 온도를 input 받고
C = int(input())            # 얼어있는 고기를 데우는데 드는 시간을 input 받고
D = int(input())            # 고기를 해동하는데 걸리는 시간을 input 받고
E = int(input())            # 얼어 있지 않은 고기를 데우는데 드는 시간을 input 받고
if A <= 0:                  # 고기가 얼어 있다면
    print(abs(A)*C+D+E*B)   # 고기를 B℃로 데우는 데 걸리는 시간을 출력한다
else:                       # 고기가 얼어있지 않다면
    print(E*(B-A))          # 고기를 B℃로 데우는 데 걸리는 시간을 출력한다