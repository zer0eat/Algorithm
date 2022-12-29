# 곱셈_BOJ1629

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
A, B, C = map(int,sys.stdin.readline().split())     # A, B, C 세 자연수를 input받고

tmp = []                                            # B가 홀수 일 때 남는 수를 저장할 빈 리스트 생성

while 1:                                            # break가 나올때까지 반복해서
    if B == 1:                                      # B가 1일 때
        A = (A % C)                                 # A를 C로 나눈 나머지로 변경하고
        break                                       # while문 break
    elif B == 2:                                    # B가 2일 때
        A = (A * A) % C                             # A를 A의 제곱을 C로 나눈 나머지로 변경하고
        break                                       # while문 break
    else:                                           # B가 그 외 일 때
        if B % 2:                                   # B가 홀수일 때
            tmp.append(A)                           # tmp에 A를 append하고
            A = (A * A) % C                         # A를 A의 제곱을 C로 나눈 나머지로 변경하고
            B //= 2                                 # B를 2로 나눈 후 나머지는 버린다
        else:                                       # B가 짝수일 때
            A = (A * A) % C                         # A를 A의 제곱을 C로 나눈 나머지로 변경하고
            B //= 2                                 # B를 2로 나눈다

for t in tmp:                                       # tmp를 반복해서
    A *= t                                          # A에 t를 곱하고
    A %= C                                          # A를 C로 나눈 나머지로 변경한다
else:                                               # 반복이 끝났으면
    print(A)                                        # A를 출력한다