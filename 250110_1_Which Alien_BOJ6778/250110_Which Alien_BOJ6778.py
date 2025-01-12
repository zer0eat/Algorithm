# Which Alien_BOJ6778

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
antena = int(input())
eye = int(input())

if antena >= 3 and eye <= 4:    # 최소 3개의 안테나와 최대 4개의 눈이 있으면
    print('TroyMartian')        # 트로이마틴을 출력하고
if antena <= 6 and eye >= 2:    # 최대 6개의 안테나와 최소 2개의 눈이 있으면
    print('VladSaturnian')      # 블라드새터니안을 출력하고
if antena <= 2 and eye <= 3:    # 최대 2개의 안테나와 최대 3개의 눈이 있으면
    print('GraemeMercurian')    # 그래미머큐리안을 출력한다