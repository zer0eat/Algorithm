# 코드마스터 2024_BOJ32215

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
n, m, k = map(int, input().split()) # n 컴퓨터 대수 / m 프로그램 수 / k 도훈이가 설치한 컴퓨터 수를 input 받고
print(m*k + m)                      # 설치 반복한 횟수를 출력한다