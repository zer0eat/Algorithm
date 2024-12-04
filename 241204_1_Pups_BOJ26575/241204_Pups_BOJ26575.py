# Pups_BOJ26575

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 테스트 케이스를 input 받고
for n in range(N):                          # 테스트 케이스를 반복해서
    d, f, p = map(float, input().split())   # 강아지의 수 / 사료양 / 사료당 가격을 input 받고
    print(f'${format(d*f*p, ".2f")}')       # 강아지를 키울 때 드는 비용을 소수 두번째자리까지 출력한다