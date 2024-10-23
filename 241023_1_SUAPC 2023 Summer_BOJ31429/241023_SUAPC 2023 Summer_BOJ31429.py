# SUAPC 2023 Summer_BOJ31429

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 등수를 input 받고
Rank = {
    1 : [12, 1600],
    2 : [11, 894],
    3 : [11, 1327],
    4 : [10, 1311],
    5 : [9, 1004],
    6 : [9, 1178],
    7 : [9, 1357],
    8 : [8, 837],
    9 : [7, 1055],
    10 : [6, 556],
    11 : [6, 773],
}                   # 등수와 패널티를 담은 딕셔너리를 생성하고
print(*Rank[N])     # 등수와 패널티를 출력한다