# 폰 노이만과 파리_BOJ14924

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S, T, D = map(int, input().split()) # S 기차의 속도, T 파리의 속도, D 기차사이의 거리를 input 받고
print(D//(2*S)*T)                   # 파리의 이동거리를 출력한다