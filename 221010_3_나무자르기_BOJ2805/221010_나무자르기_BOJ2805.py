# 나무자르기_BOJ2805

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())           # N 나무의수 / M 필요한 나무의 길이
wood = list(map(int, sys.stdin.readline().split()))     # N개의 나무의 높이를 리스트로 저장

start = 0                                               # 이분 탐색을 위한 시작 start 설정
end = max(wood)                                         # 이분 탐색을 위한 시작 end 설정

while start <= end:                                     # start가 end보다 커질때까지 반복
    middle = (start + end) // 2                         # middle 시작과 끝점을 더해서 반으로 나눈 값의 몫

    cnt = 0                                             # 자른 나무의 높이를 더할 변수
    for w in wood:                                      # 나무를 반복해서
        if (w - middle) > 0:                            # middle보다 큰나무라면
            cnt += (w - middle)                         # cnt에 자른 나무의 길이를 더한다

    else:                                               # 나무를 모두 자른 후
        if cnt == M:                                    # cnt가 필요한나무의 길이만큼 잘렸다면
            print(middle)                               # middle을 출력하고 반복문을 종료한다
            break

        elif cnt < M:                                   # cnt가 필요한 나무의 길이보다 작다면
            end = middle - 1                            # end를 middle -1 로 저장

        elif cnt > M:                                   # cnt가 필요한 나무의 길이보다 길다면
            start = middle + 1                          # end를 middle +1 로 저장
else:                                                   # start보다 end가 더 작아졌다면
    print(end)                                          # end를 출력한다