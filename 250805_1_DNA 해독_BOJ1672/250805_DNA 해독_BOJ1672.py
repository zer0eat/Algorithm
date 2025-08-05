# DNA 해독_BOJ1672

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # DNA의 길이를 input받고
DNA = list(input().strip())     # DNA를 input받고
DNA.reverse()                   # DNA를 뒤집어서
tmp = DNA[0]                    # 첫번째 염기서열을 저장하고
for n in range(1, len(DNA)):    # 염기서열을 반복해서
    if tmp == 'A':              # 현재 DNA가 A이고
        if DNA[n] == 'G':       # 다음 DNA가 G라면
            tmp = 'C'           # 현재를 C로 저장한다
        elif DNA[n] == 'T':     # 다음 DNA가 T라면
            tmp = 'G'           # 현재를 G로 저장한다
        else:                   # 다음 DNA가 A, C라면
            tmp = 'A'           # 현재를 A로 저장한다
    elif tmp == 'G':            # 현재 DNA가 G이고
        if DNA[n] == 'G':       # 다음 DNA가 G라면
            tmp = 'G'           # 현재를 G로 저장한다
        elif DNA[n] == 'A':     # 다음 DNA가 A라면
            tmp = 'C'           # 현재를 C로 저장한다
        elif DNA[n] == 'C':     # 다음 DNA가 C라면
            tmp = 'T'           # 현재를 T로 저장한다
        else:                   # 다음 DNA가 T라면
            tmp = 'A'           # 현재를 A로 저장한다
    elif tmp == 'C':            # 현재 DNA가 C이고
        if DNA[n] == 'G':       # 다음 DNA가 G라면
            tmp = 'T'           # 현재를 T로 저장한다
        elif DNA[n] == 'T':     # 다음 DNA가 T라면
            tmp = 'G'           # 현재를 G로 저장한다
        elif DNA[n] == 'A':     # 다음 DNA가 A라면
            tmp = 'A'           # 현재를 A로 저장한다
        else:                   # 다음 DNA가 G,C라면
            tmp = 'C'           # 현재를 C로 저장한다
    else:                       # 현재 DNA가 T이고
        if DNA[n] == 'G':       # 다음 DNA가 G라면
            tmp = 'A'           # 현재를 A로 저장한다
        elif DNA[n] == 'T':     # 다음 DNA가 T라면
            tmp = 'T'           # 현재를 T로 저장한다
        else:                   # 다음 DNA가 A,C라면
            tmp = 'G'           # 현재를 G로 저장한다
print(tmp)                      # 계산한 염기서열을 출력한다