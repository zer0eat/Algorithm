# 개미굴_BOJ14725

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                       # 개미굴 터널의 개수를 input 받고
food = []                                           # 개미굴의 먹이정보를 저장할 빈 리스트 생성

for t in range(T):                                  # 개미굴 터널의 수를 반복해서
    ant = list(sys.stdin.readline().split())        # 개미가 지나다니면서 확인한 먹이정보를 리스트 형태로 input 받고
    food.append(ant[1:])                            # food 리스트에 먹이의 개수만 빼고 append 한다
else:                                               # 모든 개미굴 터널을 반복했다면
    food.sort()                                     # 먹이정보를 sort하여 오름차순 정렬한다

answer = []                                         # 개미굴을 시각화한 정보를 저장하기 위한 빈 리스트 생성

for f in range(len(food)):                          # 먹이정보가 담긴 리스트를 반복해서
    if f == 0:                                      # 첫번째 먹이정보가 담긴 리스트라면
        for ant in range(len(food[f])):             # 리스트를 전부 반복해서
            answer.append('--'*ant + food[f][ant])  # 깊이별로 시각화하여 answer 리스트에 append 한다
    else:                                           # 먹이정보가 담긴 두번째 리스트 부터는
        deep = 0                                    # 공유하는 깊이를 확인하기 위한 변수를 생성하고
        for d in range(len(food[f])):               # 먹이정보가 담긴 리스트를 반복해서
            if food[f-1][d] != food[f][d] or len(food[f-1]) <= d:   # 이전 리스트와 같은 인덱스에서 먹이정보가 다르거나 이전 리스트보다 더 깊어졌다면
                break                               # 반복을 종료한다
            else:                                   # 이전 리스트와 같은 인덱스가 같은 정보라면
                deep = d + 1                        # 깊이를 다음 인덱스로 변경한다
        for ant in range(deep, len(food[f])):       # 공유하는 굴을 깊이 이후로 반복을 해서
            answer.append('--'*ant + food[f][ant])  # 깊이별로 시각화하여 answer 리스트에 append 한다
else:                                               # 모든 먹이정보를 찾았다면
    for ans in answer:                              # 정답을 반복해서
        print(ans)                                  # 시각화한 먹이정보를 출력한다