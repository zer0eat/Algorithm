# 정보보호학부 동아리 소개_BOJ28691

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
name = input().strip()  # 동아리 첫번째 글자를 input 받고
if name == 'M':         # 첫번째 글자가 M이라면
    print('MatKor')     # MatKor를 출력한다
elif name == 'W':       # 첫번째 글자가 W이라면
    print('WiCys')      # WiCys를 출력한다
elif name == 'C':       # 첫번째 글자가 C이라면
    print('CyKor')      # CyKor를 출력한다
elif name == 'A':       # 첫번째 글자가 A이라면
    print('AlKor')      # AlKor를 출력한다
elif name == '$':       # 첫번째 글자가 $이라면
    print('$clear')     # $clear를 출력한다