# Zero or One_BOJ13623

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C = map(int, input().split()) # 셋의 상태를 input 받고
if A == B and A != C:               # C가 둘과 다르다면
    print('C')                      # C를 출력한다
elif A == C and A != B:             # B가 둘과 다르다면
    print('B')                      # B를 출력한다
elif B == C and A != B:             # A가 둘과 다르다면
    print('A')                      # A를 출력한다
else:                               # 모두 같다면
    print('*')                      # *을 출력한다