# 이진수2_14142

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                        # 테스트케이스
for t in range(T):                      # 테스트 케이스를 반복할 때
    N = float(input())                  # N에 실수로 input 받음

    ans = ''                            # 이진수로 바꾼 결과를 담을 변수를 생성하고
    n = -1                              # 지수로 사용할 변수를 생성하고
    while 1:                            # break가 나올 때까지 반복한다
        if len(ans) >= 13:              # 이진수로 바꾼 결과가 13자리 이상이면
            ans = 'overflow'            # ans를 overflow로 바꾸고
            break                       # 반복문을 종료한다
        elif N - 2 ** n > 0:            # N에서 2의 n승을 뺐을 때 양수라면
            ans += '1'                  # ans에 '1'을 더하고
            N = N - 2 ** n              # N을 N - 2 ** n로 바꿔준 후
            n -= 1                      # 지수로 사용할 n을 하나 빼준다
        elif N - 2 ** n < 0:            # N에서 2의 n승을 뺐을 때 음수라면
            ans += '0'                  # ans에 '0'을 더하고
            n -= 1                      # 지수로 사용할 n을 하나 빼준다
        elif N - 2 ** n == 0:           # N에서 2의 n승을 뺐을 때 0이라면
            ans += '1'                  # ans에 '1'을 더하고 반복문을 종료한다
            break

    print(f'#{t+1}', ans)               # 이진수로 변환된 실수를 출력한다
