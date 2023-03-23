# 두수의합_BOJ3273

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # N 수열의 크기
num = list(map(int, input().split()))   # num 수열을 리스트 형태로 input
X = int(input())                        # X 두 수의 합이 되어야하는 수 

num.sort()                              # 수열을 오름차순으로 정렬한 후
A = 0                                   # A는 시작점
B = N-1                                 # B는 끝점을 가르킨다
ans = 0                                 # 두 수의 합이 X가 되는 쌍의 수를 저장할 변수 생성
while A < B:                            # A가 B와 같아질 때까지 반복해서
    sumNum = num[A] + num[B]            # A와 B가 가르키는 수의 합을 sumNum으로 저장
    if sumNum == X:                     # sumNum이 X와 같다면
        ans += 1                        # ans에 1을 추가하고
        A += 1                          # A를 오른쪽으로 한칸 이동
    elif sumNum < X:                    # sumNum이 X보다 작다면
        A += 1                          # A를 오른쪽으로 한칸 이동
    else:                               # sumNum이 X보다 크다면
        B -= 1                          # B를 왼쪽으로 한칸 이동
print(ans)                              # 두 수의 합이 X가 되는 수를 출력한다