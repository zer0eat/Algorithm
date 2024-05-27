# 운동장 한 바퀴_BOJ16486

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
d1 = int(input())           # 운동장 트랙의 한 변의 길이를 input 받고
d2 = int(input())           # 운동장 트랙의 반지름의 길이를 input 받아서
pi = 3.141592               # 파이를 변수에 저장하고
ans = (pi*d2*2) + (d1*2)    # 운동장 한바퀴의 길이를 구한 후
print(ans)                  # 운동장의 둘레를 출력한다