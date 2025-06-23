# 단어 사다리_BOJ9229

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while True:                                         # break가 나올때까지 반복해서
    word = input().strip()                          # 비교할 단어를 input받고
    if word == '#':                                 # 비교할 단어가 #이라면
        break                                       # while문을 종료한다
    flag = True                                     # 단어 사다리 구조를 표시할 변수를 생성한다
    while True:                                     # break가 나올때까지 반복해서
        next_word = input().strip()                 # 다음 단어를 input받고
        if next_word == '#':                        # 다음 단어가 #이라면
            if flag:                                # 단어 사다리 구조라면
                print('Correct')                    # correct를 출력하고
            else:                                   # 단어 사다리 구조가 아니라면
                print('Incorrect')                  # incorrect를 출력하고
            break                                   # while문을 종료한다
        if len(word) != len(next_word):             # 두 단어의 길이가 다르다면
            flag = False                            # 단어 사다리 구조가 아니라고 표시한다
        else:                                       # 두 단어의 길이가 같다면
            tmp = 0                                 # 다른 단어의 개수를 셀 변수를 생성하고
            for a in range(len(word)):              # 단어의 길이를 반복해서
                if word[a] != next_word[a]:         # 단어가 다르다면
                    tmp += 1                        # 틀린 개수를 추가하고
            if tmp != 1:                            # 틀린 개수가 1개가 아니라면
                flag = False                        # 단어 사다리 구조가 아니라고 표시한다
        word = next_word                            # 다음 단어를 현재단어로 저장한다