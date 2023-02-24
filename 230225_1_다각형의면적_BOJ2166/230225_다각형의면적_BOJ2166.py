# 다각형의면적_BOJ2166

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # N 꼭지점의 개수
vertex = [list(map(int, input().split())) for _ in range(N)]    # 꼭지점의 좌표를 리스트에 저장한다

left = 0                                                        # 가우스의 면적공식에서 왼쪽 위에서 오른쪽 아래로 내려오는 값을 저장할 변수 
right = 0                                                       # 가우스의 면적공식에서 오른쪽 위에서 왼쪽 아래로 내려오는 값을 저장할 변수

i = -1                                                          # 꼭지점을 선택하기 위한 변수1
j = 0                                                           # 꼭지점을 선택하기 위한 변수2
while j < N:                                                    # j가 N이 될 때까지 반복해서
    left += vertex[i][0] * vertex[i+1][1]                       # i점의 x 좌표와 j 점의 y 좌표의 곱을 left에 더한다
    right += vertex[i][1] * vertex[i+1][0]                      # j점의 x 좌표와 i 점의 y 좌표의 곱을 right에 더한다
    i+=1                                                        # i를 다음점으로 이동하고
    j+=1                                                        # j를 다음점으로 이동한다
else:                                                           # 반복을 마쳤다면
    print(round((abs(left-right)/2),1))                         # left와 right의 차의 절대값을 2로 나눈 값을 출력하여 다각형의 면적을 출력한다
