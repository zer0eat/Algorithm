# Darius님 한타 안 함_BOJ20499

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
k, d, a = map(int, input().split('/'))  # k 킬 d 데스 a 어시스트를 input 받고
if k + a < d or d == 0:                 # 킬과 어시시트의 합이 데스보다 작거나 데스가 0이라면
    print('hasu')                       # 하수를 출력하고
else:                                   # 그렇지 않다면
    print('gosu')                       # 고수를 출력한다