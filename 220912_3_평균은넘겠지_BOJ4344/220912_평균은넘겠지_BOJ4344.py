# 평균은넘겠지_BOJ4344

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
C = int(input())                            # 테스트 케이스
for c in range(C):                          # 테스트 케이스를 반복할 때
    arr = list(map(int, input().split()))   # 성적표 리스트를 input 받고
    ans = 0                                 # 정답을 저장할 변수와
    medi = 0                                # 평균값을 저장할 변수를 생성
    for a in range(arr[0]):                 # 성적표 맨앞에 학생의 수를 반복하여
        medi += arr[a+1]                    # 각각의 성적을 medi에 더하고
    else:                                   # 반복이 끝난 후
        medi = medi/arr[0]                  # 학생수로 나누어 평균값을 구해준다

    for a in range(arr[0]):                 # 학생 수만큼 반복하여
        if arr[a+1] > medi:                 # 평균보다 높은 성적을 가진 학생이 나오면
            ans += 1                        # ans에 추가한다
    else:                                   # 반복이 끝나면
        print(f'{ans/arr[0]*100:.3f}%')     # 그 비율을 소수 3번째자리까지 출력한다