# 적어도 대부분의 배수_BOJ1145

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
lst = list(map(int, input().split()))   # 5개의 수를 리스트로 input 받고
for i in range(4, 1000000):             # 적어도 대부분의 배수가 될 숫자를 반복해서
    cnt = 0                             # 배수의 개수를 셀 변수를 생성하고
    for l in lst:                       # input 받은 수를 반복해서
        if i%l == 0:                    # i가 input 받은 수로 나눠 떨어지면
            cnt += 1                    # 배수의 개수를 1 추가한다
    else:                               # 5개의 수를 모두 확인했다면
        if cnt >= 3:                    # 배수의 개수가 3개 이상이라면
            print(i)                    # 적어도 대부분의 배수가 되는 i를 출력하고
            break                       # for문을 종료한다