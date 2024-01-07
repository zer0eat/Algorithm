# 슈퍼마리오_BOJ2851

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                                         # 마리오가 받는 점수를 저장할 변수를 생성하고
for i in range(10):                             # 10개의 버섯을 반복해서
    mushroom = int(input())                     # 버섯의 점수를 input받는다
    if ans + mushroom >= 100:                   # 현재까지 점수와 버섯의 점수의 합이 100이상이라면
        if 100 - ans >= ans + mushroom - 100:   # 버섯을 먹은 후가 버섯을 먹기 전 점수보다 100에 가깝거나 같을 경우
            print(ans + mushroom)               # 현재까지 점수에 버섯의 점수를 더해 출력하고
        else:                                   # 버섯을 먹기 전이 버섯을 먹은 후 점수보다 100에 가까운 경우
            print(ans)                          # 현재까지 점수를 출력하고
        break                                   # for문을 종료한다
    else:                                       # 버섯을 먹어도 100점 이상이 아니라면
        ans += mushroom                         # 현재 점수에 버섯의 점수를 더한다
else:                                           # 10개를 모두 먹었다면
    print(ans)                                  # ans를 출력한다