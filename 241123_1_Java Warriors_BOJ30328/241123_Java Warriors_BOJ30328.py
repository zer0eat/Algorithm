# Java Warriors_BOJ30328

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 출전팀의 수를 input 받고
print(N*4000)       # 필요한 등록금을 출력한다