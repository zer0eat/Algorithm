# Adding Trouble_BOJ31654

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C = map(int, input().split()) # 세 정수를 input 받고
if A + B == C:                      # 두 수의 합이 정답이 되면
    print('correct!')               # correct를 출력하고
else:                               # 두 수의 합이 정답이 아니라면
    print('wrong!')                 # wrong을 출력한다