# 고대유적_9489

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스만큼 반복할 때
    N, M = map(int, input().split())                                # N = 행의 값 / M = 열의 값
    picture = [list(map(int, input().split())) for _ in range(N)]   # 사진의 데이터가 담기 행렬을 저장

    # 유적의 길이 측정하기