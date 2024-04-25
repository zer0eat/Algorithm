# 수학은 체육과목입니다_BOJ15894

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 가장 아랫 부분의 정사각형의 수를 input 받고
print(4 * N)          # 도형의 둘레를 출력한다