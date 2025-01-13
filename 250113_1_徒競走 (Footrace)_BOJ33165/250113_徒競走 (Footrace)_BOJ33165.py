# 徒競走 (Footrace)_BOJ33165

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())    # 시간을 input 받고
V = int(input())    # 속도를 input 받아서
print(T*V)          # 이동한 거리를 출력한다