# 대표값2_BOJ2587

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
arr = []                        # input받은 값을 저장할 빈 리스트를 생성하고
for _ in range(5):              # 5번을 반복해서
    arr.append(int(input()))    # arr에 input받은 값을 저장한다
else:                           # 반복을 마쳤다면
    arr.sort()                  # 오름차순으로 정렬
    print(sum(arr)//5)          # 평균을 출력
    print(arr[2])               # 중앙값을 출력
