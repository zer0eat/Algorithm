# 10!_BOJ28352

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 
N = int(input())        # 팩토리얼을 할 숫자를 input 받고
week = 60 * 60 * 24 * 7 # 한 주의 초를 저장하고
seconds = 1             # 초를 저장할 변수를 생성한다
for n in range(1, N+1): # 팩토리얼을 반복해서
    seconds *= n        # 초를 곱해준 후 후
print(seconds // week)  # N! 초가 몇 주인지 출력한다