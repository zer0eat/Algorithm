# 의석이의세로로말해요_5336

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N = 5 # 받을 단어의 수
    word = [list(input()) for _ in range(N)] # N줄을 단어를 리스트로 받아서 word에 저장
    # 가장 긴 줄의 단어 찾기
    maxV = 0
    for i in range(N):
        if len(word[i]) > maxV:
            maxV = len(word[i])
    # 단어의 길이가 가장 긴줄 보다 짧으면 짧은 만큼 빈 문자열 추가하기
    for i in range(N):
        if len(word[i]) == maxV:
            pass
        elif len(word[i]) != maxV:
            for v in range(maxV - len(word[i])):
                word[i].append('')
    # 단어를 세로로 읽어 word_col에 저장하기
    word_col = []
    for j in range(maxV):
        for i in range(N):
            word_col.append(word[i][j])

    print(f'#{t+1} ', end = '')
    print(*word_col, sep = '')



