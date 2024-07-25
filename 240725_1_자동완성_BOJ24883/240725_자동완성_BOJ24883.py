# 자동완성_BOJ24883

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word = input().strip()          # 문자를 input 받고
if word == 'N' or word == 'n':  # N 또는 n이라면
    print('Naver D2')           # Naver D2를 출력하고
else:                           # 다른 문자가 나오면
    print('Naver Whale')        # Naver whale을 출력한다