# 分 (Minutes)_BOJ31614

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
H = int(input())    # 시간을 input 받고
M = int(input())    # 분을 input 받고
print(H*60+M)       # input 받은 시간과 분이 총 몇분인지 출력한다