# 노트북 세 대를 가지고 왔다_BOJ33515

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
t1, t2 = map(int, input().split())  # 두사람이 문제를 푸는데 걸리는 시간을 input 받고
print(min(t1, t2))                  # 더 짧은 시간을 출력한다