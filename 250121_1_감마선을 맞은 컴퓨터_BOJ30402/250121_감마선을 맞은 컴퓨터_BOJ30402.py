# 감마선을 맞은 컴퓨터_BOJ30402

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
pixel = [input().split() for _ in range(15)]    # 고양이 pixel을 input 받고
for n in range(15):                             # 행을 반복하고
    for m in range(15):                         # 열을 반복해서
        if pixel[n][m] == 'w':                  # 픽셀이 w라면
            print('chunbae')                    # 춘배를 출력하고
            quit()                              # 종료한다
        elif pixel[n][m] == 'b':                # 픽셀이 b라면
            print('nabi')                       # 나비를 출력하고
            quit()                              # 종료한다
        elif pixel[n][m] == 'g':                # 픽셀이 g라면
            print('yeongcheol')                 # 영철을 출력하고
            quit()                              # 종료한다