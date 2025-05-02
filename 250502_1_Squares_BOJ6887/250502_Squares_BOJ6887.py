# Squares_BOJ6887

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
tiles = int(input())                                        # 타일의 수를 input 받고
ans = tiles**(1/2)                                          # 타일로 만들 수 있는 정사각형의 한변의 길이를 구하고
print(f'The largest square has side length {int(ans)}.')    # 정사각형의 한변의 길이 중 가장 큰 정수를 출력한다