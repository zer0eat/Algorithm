# SciComLove_BOJ21598

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 절을 할 횟수를 input 받고
for n in range(N):      # 절을 할 횟수를 반복해서
    print('SciComLove') # SciComLove을 출력한다