# AI 선도대학_BOJ32951

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 연도를 입력받고
print(N-2024)       # 흘러간 해를 출력한다