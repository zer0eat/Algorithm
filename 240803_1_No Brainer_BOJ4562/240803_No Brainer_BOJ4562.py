# No Brainer_BOJ4562

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 데이터 집합의 수를 input 받고
for n in range(N):                      # 데이터 집합의 수를 반복해서
    x, y = map(int, input().split())    # x 먹은 뇌와 y 필요한 뇌의 수를 input 받고
    if x < y:                           # 뇌가 모자라면
        print('NO BRAINS')              # NO BRAINS을 출력한다
    else:                               # 뇌가 충분하면
        print('MMM BRAINS')             # MMM BRAINS을 출력한다