# Gnome Sequencing_BOJ4589

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 그룹의 수를 input 받고
print('Gnomes:')                        # 제목줄을 출력하고
for n in range(N):                      # 그룹을 반복해서
    G = list(map(int, input().split())) # 그룹의 키를 input 받고
    S = sorted(G)                       # 오름차순 정렬하고
    U = sorted(G, reverse=True)         # 내림차순 정렬하고
    if G == S or G == U:                # 키가 정렬이 되어있다면
        print('Ordered')                # ordered를 출력하고
    else:                               # 키가 정렬이 안되어있다면
        print('Unordered')              # unordered를 출력한다