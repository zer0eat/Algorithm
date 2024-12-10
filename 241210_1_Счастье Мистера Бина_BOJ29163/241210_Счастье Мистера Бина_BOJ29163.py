# Счастье Мистера Бина_BOJ29163

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 숫자의 수를 input 받고
feels = list(map(int, input().split()))     # 숫자의 리스트를 input 받고
ans = 0                                     # 정답을 저장할 변수를 생성한다
for feel in feels:                          # 숫자를 반복해서
    if feel % 2:                            # 홀수라면
        ans -= 1                            # 감소하고
    else:                                   # 짝수라면
        ans += 1                            # 증가해서
if ans >  0:                                # 감정이 양수면
    print('Happy')                          # Happy를 출력하고
else:                                       # 감정이 0 이하라면
    print('Sad')                            # Sad를 출력한다