# 250425_1_Football Team_BOJ5358

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                # break가 나올때까지 반복해서
    try:                                # input이 있다면
        name = list(input().strip())    # 이름을 input받고
        for n in range(len(name)):      # 이름의 길이를 반복해서
            if name[n] == 'e':          # e가 나왔다면
                name[n] = 'i'           # i로 바꿔주고
            elif name[n] == 'E':        # E가 나왔다면
                name[n] = 'I'           # I로 바꿔주고
            elif name[n] == 'i':        # i가 나왔다면
                name[n] = 'e'           # e로 바꿔주고
            elif name[n] == 'I':        # I가 나왔다면
                name[n] = 'E'           # E로 바꿔주고
            print(name[n], end='')      # 이름을 붙여서 출력하고
        else:                           # 이름이 끝나면
            print()                     # 한줄 건너 뛴다
    except:                             # input이 없다면
        break                           # while문을 종료한다