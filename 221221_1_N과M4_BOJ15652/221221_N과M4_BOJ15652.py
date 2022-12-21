# N과M4_BOJ15652

# import.txt 열기
import sys
sys.stdin = open('input.txt')

def NM(s):
    if len(tmp) == M:                           # tmp 리스트에 M개의 요소가 들어있다면
        print(*tmp)                             # tmp를 출력하고
        return                                  # return한다
    for i in range(s, N + 1):                   # 1부터 N까지 반복해서
        tmp.append(i)                           # tmp에 i를 append하고
        NM(i)                                   # NM 함수를 실행하고
        tmp.pop()                               # tmp에서 i를 pop한다

# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 수열의 개수 / M 중복 없이 고를 개수

tmp = []                                        # 정답을 저장할 빈 리스트 생성

NM(1)                                            # NM 함수 실행
