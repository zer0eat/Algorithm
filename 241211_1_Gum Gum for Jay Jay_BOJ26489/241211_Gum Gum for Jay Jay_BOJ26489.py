# Gum Gum for Jay Jay_BOJ26489

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
ans = 0             # 정답을 저장할 변수를 생성하고
while 1:            # break가 나올 때까지 반복해서
    try:            # input을 받을 수 있다면
        a = input() # 문자를 input 받으면
        ans += 1    # 문자열을 1 추가한다
    except:         # input을 받을 수 없다면
        break       # while문을 break한다
print(ans)          # 총 문장의 수를 출력한다