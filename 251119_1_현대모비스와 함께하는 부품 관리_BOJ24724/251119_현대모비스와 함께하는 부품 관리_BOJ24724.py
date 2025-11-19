# 현대모비스와 함께하는 부품 관리_BOJ24724

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스 개수를 input받고
for t in range(T):                          # 테스트 케이스 개수만큼 반복하면서
    N = int(input())                        # 부품 개수를 input받고
    A, B = map(int, input().split())        # 크기제한과 무게제한을 input받고
    for n in range(N):                      # 부품 개수만큼 반복하면서
        u, v = map(int, input().split())    # 부품의 크기와 무게를 input받고
    print(f'Material Management {t + 1}')   # 테스트 케이스 번호를 출력하고
    print('Classification ---- End!')       # 종료 문구를 출력한다