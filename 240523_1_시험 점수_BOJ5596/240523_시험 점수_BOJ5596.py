# 시험 점수_BOJ5596

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = sum(list(map(int, input().split())))    # 민국이의 점수의 합을 저장하고
T = sum(list(map(int, input().split())))    # 만세의 점수의 합을 저장해서
print(max(S, T))                            # 시험을 더 잘 본 사람의 성적을 출력한다