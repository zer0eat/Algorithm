# 鉛筆 (Pencils)_BOJ15474

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, A, B, C, D = map(int, input().split())   # 사야하는 연필의 수와 세트별 가격을 input 받고
ansA, ansB = 0, 0                           # 세트별 금액을 저장할 변수를 생성하고
if N % A:                                   # A세트로 N개 만큼 살 수 없다면
    ansA = (N//A+1)*B                       # A세트의 가격을 구하고
else:                                       # A세트로 N개 만큼 살 수 있다면
    ansA = N//A*B                           # A세트의 가격을 구하고
if N % C:                                   # B세트로 N개 만큼 살 수 없다면
    ansB = (N//C+1)*D                       # B세트의 가격을 구하고
else:                                       # B세트로 N개 만큼 살 수 있다면
    ansB = N//C*D                           # B세트의 가격을 구하고
print(min(ansA, ansB))                      # 두 세트 중 N개만큼 살때 더 싼 가격을 출력한다