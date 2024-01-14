# 뒤집어진 소수_BOJ10859

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = input().strip()                 # 디지털 숫자를 input받고
if N == '1':                        # 디지털 숫자가 1이라면
    print('no')                     # 소수가 아니므로 no를 출력하고
    quit()                          # 종료한다
for i in range(2, int(N)+1):        # 2부터 N까지 반복해서
    if i * i > int(N):              # i 제곱이 N보다 크다면 더 이상 약수가 될 수 없으므로
        break                       # for문을 종료한다
    if int(N) % i == 0:             # N이 i로 나눠진다면
        print('no')                 # 소수가 아니므로 no를 출력하고
        quit()                      # 종료한다
reverseN = ''                       # 디지털 숫자를 뒤집은 수를 저장할 변수를 생성하고
for i in range(len(N)-1,-1,-1):     # 디지털 숫자를 뒤에서부터 반복해서
    if N[i] in ['3', '4', '7']:     # 3, 4, 7의 숫자가 나왔다면
        print('no')                 # 뒤집었을 때 숫자가 아니므로 no를 출력하고
        quit()                      # 종료한다
    elif N[i] == '6':               # 6이 나왔다면
        reverseN += '9'             # 뒤집었을 때 9가 되므로 9를 더해준다
    elif N[i] == '9':               # 9가 나왔다면
        reverseN += '6'             # 뒤집었을 때 6이 되므로 6을 더해준다
    else:                           # 나머지 숫자가 나왔다면
        reverseN += N[i]            # 뒤집어도 같은 숫자이므로 같은 수를 더해준다
for i in range(2, int(reverseN)+1): # 2부터 reverseN까지 반복해서
    if i * i > int(reverseN):       # i 제곱이 reverseN보다 크다면 더 이상 약수가 될 수 없으므로
        break                       # for문을 종료한다
    if int(reverseN) % i == 0:      # reverseN이 i로 나눠진다면
        print('no')                 # 소수가 아니므로 no를 출력하고
        quit()                      # 종료한다
print('yes')                        # 모든 조건을 통과 했다면 뒤집기 전 후 모두 소수이므로 yes를 출력한다