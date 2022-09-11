# 상수_BOJ2908

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
A, B = input().split()      # 두 숫자를 A, B로 input 받는다

Aans = ''                   # 상수가 읽는대로 숫자를 변환할 변수를 만든다
Bans = ''                   

for a in A:                 # A를 반복해서
    Aans = a + Aans         # 상수가 읽는대로 일의자리가 맨앞으로 오도록 숫자를 뒤집는다
for b in B:
    Bans = b + Bans

Aans = int(Aans)            # str로 변환한 숫자를 int로 바꾸고
Bans = int(Bans)

if Aans > Bans:             # 크기비교를 해서 더 큰 숫자를 출력한다
    print(Aans)
elif Aans < Bans:
    print(Bans)     