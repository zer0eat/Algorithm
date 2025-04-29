# Body Mass Index_BOJ6825

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
w = float(input())          # 몸무게를 input받고
h = float(input())          # 키를 input받고
bmi = w/(h*h)               # bmi를 구한 후
if bmi >= 25:               # 25 이상이면
    print('Overweight')     # 과체중을 출력하고
elif bmi >= 18.5:           # 18.5이상 25미만이면
    print('Normal weight')  # 정상체중을 출력하고
else:                       # 18.5 미만이면
    print('Underweight')    # 저체중을 출력한다