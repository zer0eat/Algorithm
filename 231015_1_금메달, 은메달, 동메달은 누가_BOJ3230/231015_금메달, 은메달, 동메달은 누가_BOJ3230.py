# 금메달, 은메달, 동메달은 누가_BOJ3230

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # N 1차전에 출전한 선수의 수 / M 2차전에 출전한 선수의 수
rank = []                           # 1차전 랭킹을 저장할 리스트 생성
for i in range(1, N+1):             # 1부터 N번의 선수를 반복해서
    r = int(input())                # i번째 선수의 랭킹을 input 받고
    rank.insert(r-1, i)             # 리스트에 i번째 선수의 랭킹을 insert한다
rank = rank[:M]                     # 2차전에 출전할 M명의 선수만 slice한 후
rank.reverse()                      # 꼴지 선수가 리스트의 맨 앞에 오도록 뒤집는다
rank2 = []                          # 최종 랭킹을 저장할 리스트를 생성하고
for i in rank:                      # 2차전에 출전할 선수를 반복해서
    r = int(input())                # i번째 선수의 랭킹을 input 받고
    rank2.insert(r - 1, i)          # 리스트에 i번째 선수의 랭킹을 insert한다
for r in range(3):                  # 금, 은, 동메달 선수를 반복해서
    print(rank2[r])                 # 순서대로 메달을 딴 선수의 번호를 출력한다