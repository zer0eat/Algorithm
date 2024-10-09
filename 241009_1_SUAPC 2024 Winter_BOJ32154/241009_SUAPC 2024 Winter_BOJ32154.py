# SUAPC 2024 Winter_BOJ32154

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 등수를 input 받고
rank = {            
    1:['A','B','C','D','E','F','G','H','J','L','M'],
    2:['A','C','E','F','G','H','I','L','M'],
    3:['A','C','E','F','G','H','I','L','M'],
    4:['A','B','C','E','F','G','H','L','M'],
    5:['A','C','E','F','G','H','L','M'],
    6:['A','C','E','F','G','H','L','M'],
    7:['A','C','E','F','G','H','L','M'],
    8:['A','C','E','F','G','H','L','M'],
    9:['A','C','E','F','G','H','L','M'],
    10:['A','B','C','F','G','H','L','M']
}                   # 등수별 정답 딕셔너리를 생성해서
ans = rank[N]       # N등이 맞춘 문제를 저장하고
print(len(ans))     # 맞춘 문제의 개수를 출력하고
print(*ans)         # 맞춘 문제의 종류를 출력한다