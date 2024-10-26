# 버그왕_BOJ3447

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                        # while문이 종료될 때까지 반복해서
    try:                                        # input 받을 줄이 있으면
        line = input().strip()                  # line을 input 받고
        while 1:                                # while문이 종료될 때까지 반복해서
            line2 = line.replace('BUG', '')     # BUG를 삭제하고
            if line == line2:                   # 변경 된 내용이 없다면
                break                           # while문을 종료한다
            else:                               # 변경 된 내용이 있다면
                line = line2                    # line을 line2로 바꿔 저장한다
        print(line)                             # 변경이 완료되었다면 line을 출력한다
    except:                                     # input 받을 줄이 없으면
        break                                   # while문을 종료한다