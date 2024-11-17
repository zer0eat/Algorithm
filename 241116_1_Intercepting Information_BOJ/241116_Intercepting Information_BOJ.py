# Intercepting Information_BOJ

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = list(map(int, input().split())) # 정수를 리스트로 input 받고
for n in range(8):                  # 정수를 반복해서
    if N[n] == 0 or N[n] == 1:      # 0, 1이라면
        pass                        # 넘어가고
    else:                           # 아니라면
        print("F")                  # F를 출력하고
        quit()                      # 종료한다
print("S")                          # 모두 0,1이라면 S를 출력한다