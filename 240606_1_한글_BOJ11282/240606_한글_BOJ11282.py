# 한글_BOJ11282

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 글자의 순번을 input 받고
print(chr(N+44031))     # N번째 순번의 글자를 출력한다