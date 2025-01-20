# Micromasters_BOJ33178

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 강의를 수강하는 학생을 input 받고
print(N//10)        # 학생 수의 10퍼센트를 출력한다