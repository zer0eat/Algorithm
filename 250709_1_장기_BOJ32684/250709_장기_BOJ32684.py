# 장기_BOJ32684

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = []                                                    # 정답을 저장할 리스트를 생성하고
for _ in range(2):                                          # 초나라와 한나라를 반복해서
    A = list(map(int, input().split()))                     # 남은 기물의 수를 input받고
    ans.append(A[0]*13+A[1]*7+A[2]*5+A[3]*3+A[4]*3+A[5]*2)  # 점수를 구해 저장한다
if ans[0] > ans[1]+1.5:                                     # 초나라가 점수가 높다면
    print('cocjr0208')                                      # cocjr0208을 출력하고
else:                                                       # 한나라가 점수가 높다면
    print('ekwoo')                                          # ekwoo를 출력한다