# 사랑은 고려대입니다_BOJ32384

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 문장의 반복 횟수를 input 받고
for n in range(N):                          # 문장의 반복 횟수를 반복해서
    print('LoveisKoreaUniversity', end=' ') # 문장을 출력하고 다음 문장과 한칸 띄어쓰기로 연결한다