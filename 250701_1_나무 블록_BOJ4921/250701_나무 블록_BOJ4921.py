# 나무 블록_BOJ4921

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
cnt = 1                                         # 순서를 저장할 변수를 생성하고
rules = {                                       # 블록의 규칙을 저장한 딕셔너리를 생성한다
    '1': ['4', '5'],
    '2': [],
    '3': ['4', '5'],
    '4': ['2', '3'],
    '5': ['8'],
    '6': ['2', '3'],
    '7': ['8'],
    '8': ['6', '7']
}
while 1:                                        # while문이 종료될때까지 반복해서
    block = input().strip()                     # 블록을 inputqkerh
    if block == '0':                            # 블록이 없다면
        break                                   # while문을 종료한다
    tmp = 1                                     # 블록의 상태를 저장할 변수를 생성하고
    if block[0] != '1' or block[-1] != '2':     # 처음과 끝 블록이 잘못됐다면
        tmp = 0                                 # 블록 상태를 변경한다
    else:                                       # 처음과 끝 블록이 정상이라면
        b = block[0]                            # 첫 블록을 저장하고
        for n in range(1, len(block)):          # 다음 블록부터 반복해서
            if block[n] not in rules[b]:        # 다음 블록이 맞지 않다면
                tmp = 0                         # 블록의 상태를 변경하고
                break                           # for문을 종료한다
            b = block[n]                        # 다음 블록이 맞다면 다음 블록을 저장한다
    if tmp:                                     # 블록이 정상이라면
        print(f'{cnt}. VALID')                  # 순서와 valid를 출력하고
    else:                                       # 블록이 비정상이라면
        print(f'{cnt}. NOT')                    # 순서와 not을 출력하고
    cnt += 1                                    # 순서를 더해준다