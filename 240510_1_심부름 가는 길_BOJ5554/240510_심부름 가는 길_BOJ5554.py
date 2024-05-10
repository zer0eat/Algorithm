# 심부름 가는 길_BOJ5554

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
seconds = 0                 # 정답을 저장할 변수를 생성하고
for n in range(4):          # 4곳을 이동하는 것을 반복해서
    seconds += int(input()) # 이동할때 걸리는 초를 input 받아 저장한다
print(seconds//60)          # 4곳을 이동할 때 걸리는 분과
print(seconds%60)           # 4곳을 이동할 때 걸리는 초를 출력한다