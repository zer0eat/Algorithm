# 모음의 개수_BOJ1264

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                            # break가 나올 때까지 반복할 때
    abc = list(input())             # people에 input 받을 것을 리스트 형태로 저장
    cnt = 0                         # 모음을 셀 빈 변수 생성 
    if abc[0] == '#':               # # 이 입력되면 break
        break                       
    for a in abc:                   # 입력받은 문장을 반복할 때
        if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U':
            cnt += 1                # 모음이 나오면 cnt에 1을 추가하고
    else:                           # 반복문이 끝나면 cnt를 출력한다
        print(cnt)

