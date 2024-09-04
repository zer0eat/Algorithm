# 조별과제를 하려는데 조장이 사라졌다_BOJ15727

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
L = int(input())    # 거리를 input 받고
if L % 5:           # 거리가 5의 배수가 아니라면
    print(L//5+1)   # 5씩 이동해서 갈 수 있는 최소거리와 남은 거리를 1 더한 값을 출력한다
else:               # 거리가 5의 배수라면 
    print(L//5)     # 5씩 이동해서 갈 수 있는 최소거리를 출력한다