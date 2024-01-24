# 같이 눈사람 만들래_BOJ20366

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 눈덩이의 수를 input받고
snow = list(map(int, input().split()))              # 눈덩이의 크기를 리스트로 input 받는다
snow.sort()                                         # 눈덩이를 오름차순으로 정렬하고
ans = 1e9                                           # 정답을 저장할 변수를 생성한다
for i in range(N-3):                                # 1번 눈사람을 만들기 위한 눈덩이를 하나 반복하고
    for j in range(i+3, N):                         # 1번 눈사람을 만들기 위한 다른 눈덩이를 하나 반복해서
        l = i+1                                     # 두 눈덩이 사이에서 맨 왼쪽을 가르킬 포인터를 생성하고
        r = j-1                                     # 두 눈덩이 사이에서 맨 오른쪽을 가르킬 포인터를 생성한다
        snowman1 = snow[i]+snow[j]                  # 1번 눈사람의 크기를 저장하고
        while l < r:                                # 왼쪽포인터가 오른쪽과 같아질때까지 반복해서
            snowman2 = snow[l] + snow[r]            # 2번 눈사람의 크기를 저장한 후
            if snowman1-snowman2 == 0:              # 두 눈사람의 크기가 같다면
                print(0)                            # 0을 출력하고
                quit()                              # 종료한다
            elif snowman1 - snowman2 < 0:           # 2번 눈사람이 더 크다면
                r -= 1                              # 오른쪽 포인터를 한 칸 이동하고
            else:                                   # 1번 눈사람이 더 크다면
                l += 1                              # 왼쪽 포인터를 한 칸 이동한다
            ans = min(ans, abs(snowman1-snowman2))  # 두 눈사람 크기의 차와 현재 저장된 값 중 더 작은 값으로 갱신한다
print(ans)                                          # 만들 수 있는 두 눈사람의 키 차이 중 최솟값을 나타내는 정수를 출력한다