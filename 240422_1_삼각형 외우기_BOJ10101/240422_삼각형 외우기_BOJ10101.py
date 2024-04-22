# 삼각형 외우기_BOJ10101

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
angle1 = []                     # 삼각형의 각을 저장할 리스트를 생성하고
angle2 = dict()                 # 삼각형의 각의 수를 저장할 딕셔너리를 생성한다
for n in range(3):              # 3개의 각을 반복해서
    t = int(input())            # 각을 input 받고
    angle1.append(t)            # angle1 리스트에 각을 append하고
    if angle2.get(t):           # t각이 이미 나왔다면
        angle2[t] += 1          # t가 key인 원소에 value를 1 추가하고
    else:                       # t각이 안나왔다면
        angle2[t] = 1           # t가 key인 원소에 value가 1로 새롭게 생성한다
if sum(angle1) == 180:          # 3각의 합이 180이라면
    if len(angle2) == 1:        # 3각이 모두 같다면
        print('Equilateral')    # Equilateral를 출력한다
    elif len(angle2) == 2:      # 3각 중 2각이 같다면
        print('Isosceles')      # Isosceles를 출력한다
    else:                       # 3각이 모두 다르다면
        print('Scalene')        # Scalene를 출력한다
else:                           # 3각의 합이 180이 아니라면
    print('Error')              # Error를 출력한다