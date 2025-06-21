# 카트라이더:드리프트_BOJ27522

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R, B = 0, 0                             # 점수를 저장할 변수를 생성하고
cart = []                               # 도착시간을 저장할 리스트를 생성한다
for n in range(8):                      # 8명의 참가자를 반복해서
    cart.append(list(input().split()))  # 도착시간과 팀을 리스트에 저장하고
cart.sort()                             # 순서대로 정렬한다
score = [10,8,6,5,4,3,2,1]              # 점수를 리스트로 생성해서
for c in range(8):                      # 1등부터 반복해서
    if cart[c][1] == 'R':               # 레드팀이라면
        R += score[c]                   # 레드팀에 n번째 점수를 추가하고
    else:                               # 블루팀이라면
        B += score[c]                   # 블루팀에 n번째 점수를 추가한다
if R > B:                               # 레드팀이 이겼다면
    print('Red')                        # Red를 출력하고
else:                                   # 블루팀이 이겼다면
    print('Blue')                       # Blue를 출력한다