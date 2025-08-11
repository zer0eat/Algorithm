# 욱제는 건축왕이야_BOJ15923

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0             # 정답을 저장할 변수를 생성하고
N = int(input())    # 꼭지점의 수를 input받는다
L = []              # 꼭지점의 위치를 저장할 리스트를 생성하고
for n in range(N):  # 꼭지점의 수를 반복해서
    L.append(list(map(int, input().split())))                           # 꼭지점의 좌표를 리스트에 append하고
for n in range(N):  # 꼭지점의 수를 반복해서
    ans += ((L[n-1][0]-L[n][0])**2 + (L[n-1][1]-L[n][1])**2)**(1/2)     # 두 꼭지점 사이의 길이를 더해준다
print(int(ans))     # 다각형의 총 길이를 출력한다