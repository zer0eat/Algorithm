# 소인수분해_BOJ11653

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())       # 소인수 분해할 숫자를 input 받고

ans = []                            # 소인수 분해한 숫자를 담을 리스트 생성
cnt = 2                             # 소인수 분해를 할 숫자를 담을 변수

if N == 1:                          # N이 1이면
    quit()                          # 코드를 종료

while cnt <= N:                     # N이 cnt보다 작거나 같을 때 반복해서
    if N % cnt == 0:                # cnt를 N으로 나눌 수 있다면
        ans.append(cnt)             # 소인수 분해한 수를 ans에 append 하고
        N = N//cnt                  # N을 소인수 분해한 숫자로 바꿔 저장한다
    else:                           # cnt를 N으로 나눌 수 없다면
        cnt += 1                    # cnt에 1을 추가한다

for a in ans:                       # 소인수 분해한 숫자가 담긴 ans를 반복해서
    print(a)                        # 소인수 분해한 숫자를 출력한다
