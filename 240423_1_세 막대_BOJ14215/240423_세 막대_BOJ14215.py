# 세 막대_BOJ14215

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
L = list(map(int, input().split())) # 삼각형의 세변을 리스트로 input 받고
L.sort()                            # 세 변을 오름차순으로 정렬한다
if L[0] + L[1] > L[2]:              # 작은 두변의 합이 가장 큰 변보다 크다면
    print(sum(L))                   # 삼각형을 만들 수 있으므로 세변의 합을 출력한다
else:                               # 가장 큰 변이 작은 두변의 합 이상이라면
    print(2*(L[0] + L[1])-1)        # 가장 큰 변이 두변의 합보다 작아야 하므로 작은 두변의 합*2에서 1을 뺀 값을 출력한다