# 사토르 마방진_BOJ20112

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 마방진의 길이를 input 받고
word = [list(input().strip()) for _ in range(N)]    # 마방진을 리스트로 input 받고
for n in range(N):                                  # 마방진의 시작점을 반복하고
    for k in range(N):                              # 마방진의 길이를 반복해서
        if word[n][k] == word[k][n]:                # 사토르 마방진을 만족하면
            pass                                    # pass하고
        else:                                       # 사토르 마방진을 만족하지 않으면
            print('NO')                             # NO를 출력하고
            quit()                                  # 종료한다
print('YES')                                        # 사토르 마방진이라면 YES를 출력한다