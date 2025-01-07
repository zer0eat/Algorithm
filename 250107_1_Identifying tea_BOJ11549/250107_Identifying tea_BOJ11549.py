# Identifying tea_BOJ11549

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 차의 종류를 input 받고
tea = list(map(int, input().split()))   # 차를 리스트로 input 받아서
print(tea.count(T))                     # 같은 종류의 차의 수를 출력한다