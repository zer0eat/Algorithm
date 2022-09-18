# 직각삼각형_BOJ4153

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                                            # break까지 반복할 때
    triangle = list(map(int, input().split()))                      # input을 triangle에 리스트로 받고
    if triangle == [0, 0, 0]:                                       # 받은 리스트가 모두 0 이면 반복문 종료
        break
    else:                                                           # 만약 리스트가 0이 아니라면
        triangle.sort()                                             # 크기 순으로 정렬하고
        if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:       # 피타고라스 정리를 만족하면
            print('right')                                          # right 출력
        else:                                                       # 만족하지 않는다면
            print('wrong')                                          # wrong 출력