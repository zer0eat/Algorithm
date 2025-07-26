# 이상한 나라의 암호_BOJ18245

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
tmp = 2                                     # 암호문의 순서를 저장할 변수를 생성하고
while 1:                                    # 암호문의 수를 반복해서
    say = list(input().strip())             # 암호문을 input받고
    if say == list('Was it a cat I saw?'):  # 암호문이 팰린드롬 특정 문장이라면
        break                               # while문을 종료한다
    for n in range(0, len(say), tmp):       # 암호문을 순서만큼 건너 뛰면서
        print(say[n], end = '')             # 암호문을 출력하고
    else:                                   # 하나의 암호가 끝났다면
        tmp += 1                            # 암호문의 번호를 하나 추가하고
        print()                             # 줄을 바꿔준다