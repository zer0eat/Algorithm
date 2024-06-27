# 다각형_BOJ11896

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a, b = map(int, input().split())    # 시작과 끝을 input 받고
if a < 3:                           # 시작점이 다각형을 만들 수 없다면
    a = 4                           # 사각형부터 시작하도록 시작점을 바꾸고
if b < 3:                           # 끝점이 다각형을 만들 수 없다면
    print(0)                        # 한개의 선으로 모든 변을 자를 수 있는 다각형이 없으므로 0을 출력하고
    quit()                          # 종료한다
if a % 2 != 0:                      # 시작점이 짝수가 아니라면
    a += 1                          # 변 한개를 추가하고
if b % 2 != 0:                      # 끝점이 짝수가 아니라면
    b -= 1                          # 변 하개를 빼준다
print(((b-a)//2+1)*(a+b)//2)        # a, b 사이의 짝수개의 변을 갖는 다각형의 수를 출력한다