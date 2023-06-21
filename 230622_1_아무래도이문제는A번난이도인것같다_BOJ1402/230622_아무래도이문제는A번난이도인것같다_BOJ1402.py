# 아무래도이문제는A번난이도인것같다_BOJ1402

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스를 input 받고
for t in range(T):                      # 테스트 케이스를 반복해서
    A, B = map(int, input().split())    # A = a1 * a2 * a3 * a4 ... * an / B = a1 + a2 + a3 ... + an 를 input 받고
    print('yes')                        # A에 1과 -1을 원하는 만큼 곱하면 항상 B를 만들 수 있으므로 yes를 출력한다