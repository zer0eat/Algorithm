# 카드숫자곱의경우의수_BOJ25370

# input.txt
import sys
sys.stdin = open('input2.txt')

# input 받기
N = int(input())                    # 선택할 카드의 개수
tmp = 0                             # 뽑은 숫자카드를 나태 낼 변수
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # 카드를 담은 리스트
ans = set()                         # 정답을 담을 빈 set을 생성
if N >= 1:                          # 뽑을 카드의 개수가 1 이상일 때
    for a in arr:                   # arr에서 카드를 뽑아
        tmp = a                     # tmp에 저장한 후
        if N == 1:                  # N이 1이면
            ans.add(tmp)            # ans에 카드를 저장
        elif N >= 2:                # N이 2 이상이면
            for b in arr:           # 다른 카드 하나를 뽑아
                tmp2 = tmp * b      # tmp에 새로 뽑은 카드를 곱해 tmp2에 저장한다
                if N == 2:          # N이 2이면
                    ans.add(tmp2)   # ans에 카드를 저장
                elif N >= 3:        # N이 3 이상이면 위와 같은 과정을 반복
                    for c in arr:
                        tmp3 = tmp2 * c
                        if N == 3:
                            ans.add(tmp3)
                        elif N >= 4:
                            for d in arr:
                                tmp4 = tmp3 * d
                                if N == 4:
                                    ans.add(tmp4)
                                elif N >= 5:
                                    for e in arr:
                                        tmp5 = tmp4 * e
                                        if N == 5:
                                            ans.add(tmp5)
                                        elif N >= 6:
                                            for f in arr:
                                                tmp6 = tmp5 * f
                                                if N == 6:
                                                    ans.add(tmp6)
                                                elif N >= 7:
                                                    for g in arr:
                                                        tmp7 = tmp6 * g
                                                        ans.add(tmp7)
print(len(ans))