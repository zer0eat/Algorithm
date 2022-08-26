# 최대성적표만들기_4466

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스만큼 반복할 때
    N, K = map(int, input().split())            # N = 받은 성적의 수/ K = 합할 성적의 수
    score = list(map(int, input().split()))     # score = 받은 성적을 리스트로 저장

    # 버블 솔트                                  # 맨앞이 가장 큰 수로 정렬
    for i in range(N-1):                        # 원소의 개수보다 하나 적게 반복하고
        for j in range(N-i-1):                  # 정렬되지 않은 원소만큼 반복
            if score[j] < score[j + 1]:         # 만약 앞의 요소가 뒤의 요소보다 작을 때
                score[j], score[j + 1] = score[j + 1], score[j]     # 앞 뒤를 바꿔준다

    # 가장 큰 점수부터 K개의 합 구하기
    max_score = 0                               # 최대 값을 저장할 변수를 생성
    for k in range(K):                          # 받은 성적을 합할 K개 만큼 반복할 때
        max_score += score[k]                   # 가장 큰수부터 K개를 max_score에 더해준다

    print(f'#{t+1}', max_score)                 # max_score 출력