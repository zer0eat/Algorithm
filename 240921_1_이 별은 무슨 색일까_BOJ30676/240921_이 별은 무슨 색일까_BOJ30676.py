# 이 별은 무슨 색일까_BOJ30676

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ramda = int(input())                # 파장의 길이를 input 받고
if 620 <= ramda and ramda <= 780:   # 620nm 이상 780nm 이하의 파장이라면
    print('Red')                    # 빨간색을 출력한다
elif 590 <= ramda and ramda < 620:  # 590nm 이상 620nm 미만의 파장이라면
    print('Orange')                 # 주황색을 출력한다
elif 570 <= ramda and ramda < 590:  # 570nm 이상 590nm 미만의 파장이라면
    print('Yellow')                 # 노란색을 출력한다
elif 495 <= ramda and ramda < 570:  # 495nm 이상 570nm 미만의 파장이라면
    print('Green')                  # 초록색을 출력한다
elif 450 <= ramda and ramda < 495:  # 450nm 이상 495nm 미만의 파장이라면
    print('Blue')                   # 파랑색을 출력한다
elif 425 <= ramda and ramda < 450:  # 425nm 이상 450nm 미만의 파장이라면
    print('Indigo')                 # 남색을 출력한다
elif 380 <= ramda and ramda < 425:  # 380nm 이상 425nm 미만의 파장이라면
    print('Violet')                 # 보라색을 출력한다